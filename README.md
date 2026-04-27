# Career Planner 🎯

> AI-powered career planning & job search assistant — an OpenClaw skill.

---

## Overview

**Career Planner** is a structured 3-step career guidance skill for [OpenClaw](https://github.com/openclaw/openclaw) AI agents. It helps users assess their background, discover relevant job opportunities, and generate professional resumes — all within a conversational interface.

### Flow

```
Step 1: Background Assessment  →  Step 2: Job Market Research  →  Step 3: Resume Generation
       (questionnaire)               (web search + Excel)            (tailored templates)
```

---

## Features

### 📋 Step 1 — Background Assessment
A conversational questionnaire covering:
- Education (degree, major, institution, year)
- Work experience and internships
- Technical & soft skills
- Career preferences (role type, location, salary, work arrangement)
- Short-term and long-term goals

### 🔍 Step 2 — Job Market Research
- Web searches across LinkedIn, BOSS直聘, 猎聘, company career pages, etc.
- Outputs a formatted **`jobs.xlsx`** spreadsheet with:
  - Job Title, Company, Location
  - Job Type, Work Arrangement
  - Required Skills & Education
  - Salary Range & Application Links
  - Deadlines & Notes

### 📝 Step 3 — Resume Generation
Three templates to choose from:
| Template | File | Best For |
|----------|------|----------|
| Modern | `assets/resume_template_modern.md` | Tech / general |
| Traditional | `assets/resume_template_traditional.md` | Conservative industries |
| Creative | `assets/resume_template_creative.md` | Design / creative roles |

Resumes are tailored to the user's background and target job types.

---

## File Structure

```
career-planner/
├── SKILL.md                      # OpenClaw skill definition
├── README.md                     # This file
├── LICENSE.txt                   # MIT License
├── jobs.xlsx                     # Generated job spreadsheet
├── resume_zh.md                  # Generated resume (Chinese example)
├── assets/
│   ├── resume_template_modern.md
│   ├── resume_template_traditional.md
│   └── resume_template_creative.md
├── references/
│   └── questionnaire_guide.md    # Full question set & tips
└── scripts/
    ├── generate_excel.py         # Python: generate formatted jobs.xlsx
    └── generate_jobs.py          # Example script for Chinese job data
```

---

## Usage (with OpenClaw)

1. **Install the skill** in your OpenClaw workspace
2. Start a conversation like:
   > _"Help me find software engineering jobs in San Francisco"_
   > _"I need a resume for marketing positions"_
   > _"What career options match my background in biology?"_

The agent will walk through the 3-step flow interactively.

### Standalone Scripts

```bash
# Generate a template jobs.xlsx (with sample data)
python scripts/generate_excel.py --sample -o jobs.xlsx

# Generate from a JSON file
python scripts/generate_excel.py --input data.json -o jobs.xlsx
```

---

## Requirements

- Python 3.8+
- `pandas`, `openpyxl` or `xlsxwriter` (for Excel generation)
- OpenClaw agent (for conversational flow)
- Web search capability (Tavily API, Brave Search, etc.)

---

## Output Examples

### jobs.xlsx Preview
| Job Title | Company | Location | Key Skills | Salary |
|-----------|---------|----------|------------|--------|
| 具身智能算法实习生 | 某深圳A轮公司 | 深圳 | Python, C++, ML | 3-8k/月 |
| 软件开发实习生 | 迈锐博机器人 | 上海 | Python, C++, ROS | 150-200元/天 |
| 嵌入式实习生 | 逐际动力(LimX) | 深圳南山 | STM32, C++, 机器人 | 面议 |

### Resume Output
A tailored markdown resume that can be exported to PDF or further customized.

---

## Customization

- **Questionnaire**: Edit `references/questionnaire_guide.md` to add/modify questions
- **Templates**: Edit files in `assets/` to change resume layout/style
- **Excel format**: Modify `scripts/generate_excel.py` to add columns or change styling

---

## License

MIT — see [LICENSE.txt](./LICENSE.txt)

---

## Contributing

PRs welcome! Ideas for improvement:
- More resume templates (LaTeX, HTML, PDF generation)
- Integration with LinkedIn API or job board APIs
- Application tracking / follow-up reminders
- Multi-language support
