# Project 4: Research Brief — Choosing Between Cloud AI and Local Model Deployment

**Research type:** Desk-research decision brief.  
**Audience:** Non-technical professionals and small organisations evaluating AI tools.  
**Question:** What should a user compare before choosing a provider-hosted AI assistant or a locally run model?

## Executive summary

Cloud-hosted AI services and locally run models involve different trade-offs, but neither category is automatically more secure, cheaper or more capable. A meaningful decision depends on the model, deployment architecture, licence, data sensitivity, device capability, connectivity, support requirements and total cost.

The most important correction to the original comparison is conceptual: “open-source model”, “open-weight model”, “local deployment” and “offline operation” are not interchangeable terms.

## Definitions that matter

- **Cloud-hosted service:** A model or application is accessed over a network and some processing is performed on infrastructure controlled by a provider.
- **Locally run model:** Model inference runs on hardware controlled by the user or organisation. Local execution may still depend on external services for updates, authentication or other functions.
- **Open-weight model:** Model parameters are available under stated terms. Access to weights alone does not necessarily provide the data and code required to study or modify the system in the full open-source sense.
- **Open-source AI system:** The Open Source Initiative's Open Source AI Definition describes the components and freedoms required for a system to qualify. The label should not be applied to every model with downloadable weights.

## Comparison framework

| Criterion | Cloud-hosted service | Local deployment |
|---|---|---|
| Initial setup | Often accessible through a browser or app; provider manages infrastructure | Requires installation, model download, configuration and compatible hardware |
| Compute and storage | Usually handled by provider; limits and price depend on plan or usage | User supplies storage and compute; model size and performance vary |
| Data handling | Depends on provider retention, training, access and contractual terms | Can reduce transmission to a model provider, but local logs, backups, devices and networks still need protection |
| Connectivity | Usually needs internet access for hosted inference | Inference can work offline after setup if the complete workflow has no external dependency |
| Maintenance | Provider operates service infrastructure; user still manages account, access and settings | User or operator manages runtime, model files, updates, security and monitoring |
| Customisation | Depends on API, product features and plan | May allow more configuration, but fine-tuning and integration require capability and resources |
| Cost | Subscription or usage charges may apply | Hardware, energy, storage, maintenance and licence costs still apply |

## Key findings

### 1. “Open” needs a precise definition

The Open Source AI Definition identifies model architecture, parameters, inference code and information about training data as relevant components. A downloadable model weight file by itself is not enough to establish that an AI system is open source. Some model providers also impose licence terms or use policies that must be reviewed before commercial use.

### 2. Local execution changes the data path, not every security risk

Running inference locally can reduce the need to send prompts to an external inference provider. It does not guarantee complete privacy or data sovereignty. The application may log prompts; the computer may be shared; backups may sync to cloud storage; and other integrations may transmit information. Security depends on the whole system and its operating practices.

### 3. Hardware requirements vary substantially

Model size, quantisation, context length, concurrent requests and runtime affect memory and performance. A lightweight model may run on modest hardware, while a larger model may require substantial RAM, GPU memory and storage. Published example sizes are not universal minimum device requirements.

### 4. “Free model” does not mean zero operating cost

A model may be available without a per-token provider bill, but local deployment still uses electricity, storage, hardware and maintenance time. Licence conditions may also affect how a model can be used or redistributed.

## Practical decision sequence

1. Classify the information and define what data may be entered into an AI tool.
2. Identify the actual task and quality requirements.
3. Compare named models and services—not just broad categories.
4. Read the exact model and software licence, privacy terms and retention controls.
5. Estimate the total cost, including hardware, subscriptions, usage, energy and maintenance.
6. Test representative low-risk tasks and measure accuracy, latency and failure modes.
7. Confirm how users can update, delete, export and protect their data.

## Sources

- [Open Source Initiative — Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition).
- [Open Source Initiative — Open Source AI FAQs](https://opensource.org/ai/faq).
- [Ollama — official downloads and deployment information](https://ollama.com/download).
- [Ollama — official model/runtime documentation](https://github.com/ollama/ollama/blob/main/docs/faq.mdx).
- [Meta — Llama model access and licence information](https://dev.meta.ai/llama/docs/getting-the-models/meta).

These sources describe definitions and selected provider/runtime examples. They do not establish a universal performance, cost or privacy outcome for all cloud or local deployments.

## Limitations

This is desk research and a decision framework, not a comparative benchmark. No named model was installed, no hardware benchmark was run and no privacy/security audit was conducted. A stronger follow-up would choose two named models, document their exact licences and system requirements, then run a controlled test on identified hardware.

**Portfolio purpose:** Demonstrates careful terminology, evidence-based comparison, qualification of overbroad claims and a practical decision framework.
