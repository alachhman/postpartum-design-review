# Postpartum weight & wellness app — design exploration

Design review site for the iOS MVP of a breastfeeding-safe nutrition coach.
Every screen in the MVP designed three times, as three coherent directions that
take different positions on the central problem: what the home-screen number is,
and what it means when she goes under it.

## What's here

| Path | |
|---|---|
| `index.html` | Overview — the three directions and the decisions they force |
| `01-home.html` … `08-adapted.html` | The screens, three directions each |
| `docs/` | The source context documents, rendered readable |
| `claude_design_context/` | Those documents in their original markdown |
| `css/dir-a.css` `dir-b.css` `dir-c.css` | The three design systems |
| `CONTRACT.md` | The build contract the mocks were produced against |
| `build_docs.py` | Renders `claude_design_context/*.md` into `docs/` |

## Running locally

```bash
python3 -m http.server 8731
```

Then open <http://localhost:8731>.

To re-render the context documents after editing the markdown:

```bash
python3 -m venv .venv && .venv/bin/pip install markdown && .venv/bin/python build_docs.py
```

## Verification harness

Any page accepts two query parameters:

- `?shot=<n>` isolates the nth phone mock at 1:1 for screenshotting
- `?audit=1` reports content overflowing the 852pt screen and any tap target under 44pt

```bash
./scripts/audit.sh 01-home.html
```

## Status

Exploration, not a spec. The app is unnamed and all wordmarks are placeholders.
Clinical coefficients are placeholders pending RD and IBCLC sign-off.
