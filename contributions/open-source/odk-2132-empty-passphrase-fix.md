# ODK Central documentation — Issue #2132

**Upstream:** getodk/docs  
**Issue:** https://github.com/getodk/docs/issues/2132  
**Issue opened:** 19 November 2026  
**Status:** Proposed patch prepared; not yet submitted upstream.

## Verified problem

The current documentation's decrypt-and-verify examples rely on an interactive empty passphrase (pressing Enter). The issue reporter states that this fails, and proposes explicitly passing an empty value.

## Proposed change

In `docs/central-backup.rst`, use the OpenSSL option `-pass pass:` for both commands where an empty passphrase is intended.

Proposed replacement for the first command:

```bash
openssl enc -d -chacha20 -pbkdf2 -pass pass: < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin | pg_restore --file /dev/null
```

Proposed replacement for the diagnostic command:

```bash
openssl enc -d -chacha20 -pbkdf2 -pass pass: < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin 2>/dev/null | head -c 5
```

Replace the existing sentence about pressing Enter with:

> If you did not use a passphrase when creating the backup, specify an empty passphrase with `-pass pass:` as shown in the commands above.

## Evidence and limitations

- Confirmed the issue is open and was created on 19 November 2026.
- Confirmed the current source text in `docs/central-backup.rst` matches the reported behavior and examples.
- Confirmed no issue comments and no matching pull request found in the search performed.
- This is a proposed change based on the issue report and source inspection. **The commands have not been executed against an actual backup file.** The patch should be validated with OpenSSL against a no-passphrase test backup before upstream submission, if a suitable test fixture is available.

## Patch

```diff
-    ``openssl enc -d -chacha20 -pbkdf2 < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin | pg_restore --file /dev/null``
+    ``openssl enc -d -chacha20 -pbkdf2 -pass pass: < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin | pg_restore --file /dev/null``

-    It will ask for the backup passphrase. Just press the ``enter`` key if you didn't use any passphrase.
+    If you did not use a passphrase when creating the backup, specify an empty passphrase with ``-pass pass:`` as shown in the commands above.

-      ``openssl enc -d -chacha20 -pbkdf2 < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin 2>/dev/null | head -c 5``
+      ``openssl enc -d -chacha20 -pbkdf2 -pass pass: < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin 2>/dev/null | head -c 5``
```
