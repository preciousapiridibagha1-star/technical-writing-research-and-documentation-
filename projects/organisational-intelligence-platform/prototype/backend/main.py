from datetime import date
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


app = FastAPI(
    title="Organisational Intelligence Platform API",
    description=(
        "An early proof of concept using fictional programme data. "
        "Not a production service and not connected to an AI model."
    ),
    version="0.1.0",
)

SECTORS = {
    "public-health": {
        "name": "Public Health",
        "description": "Community outreach and prevention programme monitoring.",
    },
    "health-organisations": {
        "name": "Health Organisation Programmes",
        "description": "Facility support, workforce training and service-improvement activities.",
    },
    "education": {
        "name": "Education",
        "description": "School support, teacher development and learning programme monitoring.",
    },
}

# Fictional demonstration records only. These are not real organisations or beneficiaries.
PROGRAMMES = [
    {
        "id": "PH-001",
        "sector": "public-health",
        "name": "Community Health Outreach",
        "organisation": "Example Community Health Initiative",
        "status": "active",
        "start_date": "2026-01-01",
        "end_date": "2026-12-31",
        "activities": [
            {"id": "PH-A1", "name": "Community outreach sessions", "status": "in_progress", "due_date": "2026-11-30"},
            {"id": "PH-A2", "name": "Health education materials distribution", "status": "completed", "due_date": "2026-10-31"},
            {"id": "PH-A3", "name": "Monthly monitoring update", "status": "overdue", "due_date": "2026-10-31"},
        ],
        "indicators": [
            {"id": "PH-I1", "name": "People reached", "unit": "people", "target": 1000, "actual": 720, "period": "2026-Q4", "updated": True},
            {"id": "PH-I2", "name": "Outreach sessions delivered", "unit": "sessions", "target": 40, "actual": 28, "period": "2026-Q4", "updated": True},
            {"id": "PH-I3", "name": "Communities with complete reports", "unit": "communities", "target": 12, "actual": None, "period": "2026-Q4", "updated": False},
        ],
    },
    {
        "id": "HO-001",
        "sector": "health-organisations",
        "name": "Facility Support and Improvement",
        "organisation": "Example Health Support Organisation",
        "status": "active",
        "start_date": "2026-02-01",
        "end_date": "2026-12-31",
        "activities": [
            {"id": "HO-A1", "name": "Facility support visits", "status": "in_progress", "due_date": "2026-12-10"},
            {"id": "HO-A2", "name": "Health workforce training", "status": "completed", "due_date": "2026-10-15"},
            {"id": "HO-A3", "name": "Service-improvement review", "status": "in_progress", "due_date": "2026-12-05"},
        ],
        "indicators": [
            {"id": "HO-I1", "name": "Facilities supported", "unit": "facilities", "target": 20, "actual": 14, "period": "2026-Q4", "updated": True},
            {"id": "HO-I2", "name": "Training sessions delivered", "unit": "sessions", "target": 10, "actual": 8, "period": "2026-Q4", "updated": True},
            {"id": "HO-I3", "name": "Facilities submitting review updates", "unit": "facilities", "target": 20, "actual": None, "period": "2026-Q4", "updated": False},
        ],
    },
    {
        "id": "ED-001",
        "sector": "education",
        "name": "School Support and Teacher Development",
        "organisation": "Example Learning Support Initiative",
        "status": "active",
        "start_date": "2026-01-15",
        "end_date": "2026-12-15",
        "activities": [
            {"id": "ED-A1", "name": "Teacher development workshops", "status": "completed", "due_date": "2026-10-20"},
            {"id": "ED-A2", "name": "School support visits", "status": "in_progress", "due_date": "2026-11-28"},
            {"id": "ED-A3", "name": "Term progress data submission", "status": "overdue", "due_date": "2026-10-30"},
        ],
        "indicators": [
            {"id": "ED-I1", "name": "Schools supported", "unit": "schools", "target": 30, "actual": 22, "period": "2026-Q4", "updated": True},
            {"id": "ED-I2", "name": "Teachers trained", "unit": "teachers", "target": 150, "actual": 110, "period": "2026-Q4", "updated": True},
            {"id": "ED-I3", "name": "Schools with submitted progress data", "unit": "schools", "target": 30, "actual": None, "period": "2026-Q4", "updated": False},
        ],
    },
]


class ProgressUpdate(BaseModel):
    indicator_id: str
    actual: float = Field(ge=0)
    reporting_period: str = Field(min_length=4, max_length=20)
    evidence_note: str = Field(min_length=3, max_length=500)


def find_programme(sector: str) -> dict:
    if sector not in SECTORS:
        raise HTTPException(status_code=404, detail="Sector configuration not found.")
    for programme in PROGRAMMES:
        if programme["sector"] == sector:
            return programme
    raise HTTPException(status_code=404, detail="No demonstration programme found.")


def progress_percent(indicator: dict) -> Optional[float]:
    target = indicator["target"]
    actual = indicator["actual"]
    if actual is None or target <= 0:
        return None
    return round((actual / target) * 100, 1)


@app.get("/")
def root():
    return {
        "service": "Organisational Intelligence Platform API",
        "status": "proof_of_concept",
        "notice": "Synthetic demonstration data only; not production-ready.",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}


@app.get("/api/v1/sectors")
def list_sectors():
    return [
        {"id": sector_id, **details}
        for sector_id, details in SECTORS.items()
    ]


@app.get("/api/v1/programmes")
def list_programmes(sector: Optional[str] = Query(default=None)):
    if sector and sector not in SECTORS:
        raise HTTPException(status_code=404, detail="Sector configuration not found.")
    selected = [
        programme for programme in PROGRAMMES
        if sector is None or programme["sector"] == sector
    ]
    return [
        {
            "id": p["id"],
            "sector": p["sector"],
            "name": p["name"],
            "organisation": p["organisation"],
            "status": p["status"],
        }
        for p in selected
    ]


@app.get("/api/v1/programmes/{programme_id}")
def programme_detail(programme_id: str):
    for programme in PROGRAMMES:
        if programme["id"] == programme_id:
            return programme
    raise HTTPException(status_code=404, detail="Programme not found.")


@app.get("/api/v1/dashboard/{sector}")
def sector_dashboard(sector: str):
    programme = find_programme(sector)
    indicators = programme["indicators"]
    activities = programme["activities"]
    completed = sum(1 for item in activities if item["status"] == "completed")
    overdue = sum(1 for item in activities if item["status"] == "overdue")
    measurable = [progress_percent(item) for item in indicators]
    measurable = [value for value in measurable if value is not None]

    return {
        "sector": SECTORS[sector]["name"],
        "programme": programme["name"],
        "active_programmes": 1 if programme["status"] == "active" else 0,
        "activities_total": len(activities),
        "activities_completed": completed,
        "activities_overdue": overdue,
        "indicators_total": len(indicators),
        "indicators_missing_updates": sum(1 for item in indicators if not item["updated"]),
        "average_reported_target_progress_percent": (
            round(sum(measurable) / len(measurable), 1) if measurable else None
        ),
        "reporting_period": "2026-Q4",
        "note": "Average excludes indicators without an actual value.",
    }


@app.get("/api/v1/data-quality/{sector}")
def data_quality(sector: str):
    programme = find_programme(sector)
    issues = []
    for indicator in programme["indicators"]:
        if not indicator["updated"] or indicator["actual"] is None:
            issues.append({
                "type": "missing_indicator_update",
                "record_id": indicator["id"],
                "message": f"No actual value has been recorded for '{indicator['name']}'.",
                "severity": "review_required",
            })
        elif indicator["actual"] > indicator["target"]:
            issues.append({
                "type": "value_above_target",
                "record_id": indicator["id"],
                "message": f"'{indicator['name']}' is above its target; confirm the value and target.",
                "severity": "check",
            })

    for activity in programme["activities"]:
        if activity["status"] == "overdue":
            issues.append({
                "type": "overdue_activity",
                "record_id": activity["id"],
                "message": f"'{activity['name']}' is marked overdue.",
                "severity": "review_required",
            })

    return {"programme_id": programme["id"], "issues_count": len(issues), "issues": issues}


@app.post("/api/v1/programmes/{programme_id}/progress")
def record_progress(programme_id: str, update: ProgressUpdate):
    for programme in PROGRAMMES:
        if programme["id"] != programme_id:
            continue
        for indicator in programme["indicators"]:
            if indicator["id"] == update.indicator_id:
                indicator["actual"] = update.actual
                indicator["period"] = update.reporting_period
                indicator["updated"] = True
                indicator["evidence_note"] = update.evidence_note
                return {
                    "message": "Progress recorded in the in-memory demonstration dataset.",
                    "indicator": indicator,
                    "progress_percent": progress_percent(indicator),
                }
        raise HTTPException(status_code=404, detail="Indicator not found for this programme.")
    raise HTTPException(status_code=404, detail="Programme not found.")


@app.get("/api/v1/intelligence/{sector}")
def answer_question(
    sector: str,
    question: str = Query(min_length=3, max_length=300),
):
    programme = find_programme(sector)
    text = question.lower()

    if "overdue" in text:
        overdue = [a["name"] for a in programme["activities"] if a["status"] == "overdue"]
        answer = ", ".join(overdue) if overdue else "No activities are marked overdue."
        basis = "activity status fields"
    elif "missing" in text or "gap" in text or "incomplete" in text:
        missing = [i["name"] for i in programme["indicators"] if not i["updated"]]
        answer = ", ".join(missing) if missing else "No missing indicator updates are recorded."
        basis = "indicator update status"
    elif "progress" in text or "target" in text:
        values = [
            f"{i['name']}: {i['actual']} of {i['target']} {i['unit']} ({progress_percent(i)}%)"
            for i in programme["indicators"] if i["actual"] is not None
        ]
        answer = "; ".join(values) if values else "There are no reported indicator values."
        basis = "recorded indicator values and deterministic target calculations"
    else:
        answer = (
            "This proof of concept can answer questions about overdue activities, "
            "missing indicator updates and recorded progress. Try asking about one of those."
        )
        basis = "supported demonstration question types"

    return {
        "question": question,
        "answer": answer,
        "programme_id": programme["id"],
        "evidence_basis": basis,
        "limitation": "Rule-based demonstration response; no language model is connected.",
    }


@app.get("/api/v1/reports/draft/{sector}")
def draft_report(sector: str):
    programme = find_programme(sector)
    dashboard = sector_dashboard(sector)
    quality = data_quality(sector)
    lines = [
        f"# Draft Programme Update: {programme['name']}",
        "",
        f"**Organisation:** {programme['organisation']}",
        "**Reporting period:** 2026-Q4",
        "",
        "## Implementation overview",
        f"The programme has {dashboard['activities_total']} listed activities. "
        f"{dashboard['activities_completed']} are marked completed and "
        f"{dashboard['activities_overdue']} are marked overdue.",
        "",
        "## Indicator progress",
    ]

    for indicator in programme["indicators"]:
        value = "Not reported"
        percentage = progress_percent(indicator)
        if indicator["actual"] is not None:
            value = f"{indicator['actual']} / {indicator['target']} {indicator['unit']}"
            if percentage is not None:
                value += f" ({percentage}% of target)"
        lines.append(f"- **{indicator['name']}:** {value}.")

    lines.extend(["", "## Data-quality notes"])
    if quality["issues"]:
        for issue in quality["issues"]:
            lines.append(f"- {issue['message']}")
    else:
        lines.append("- No data-quality flags were returned by the demonstration rules.")

    lines.extend([
        "",
        "## Review note",
        "This is a rule-generated draft based only on the fictional records in this proof of concept. "
        "A programme team must verify the data and approve any report before external use.",
    ])
    return {
        "programme_id": programme["id"],
        "reporting_period": "2026-Q4",
        "draft_markdown": "\n".join(lines),
        "source_record_ids": [
            *(a["id"] for a in programme["activities"]),
            *(i["id"] for i in programme["indicators"]),
        ],
        "status": "draft_for_human_review",
    }
