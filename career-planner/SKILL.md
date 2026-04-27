---
name: career-planner
description: Comprehensive career planning and job search assistance. Use when a user needs help with: (1) Career assessment and background analysis, (2) Job search and opportunity discovery, (3) Resume creation and optimization. This skill guides users through a structured career planning process including background questionnaire, job market research, and personalized resume generation.
---

# Career Planner

## Overview

This skill provides a complete career planning workflow to help users identify suitable job opportunities and create professional application materials. It follows a three-step process: background assessment, job market research, and resume generation.

## Workflow

### Step 1: Background Assessment
Start by generating a comprehensive career background questionnaire to understand the user's profile:
- **Education**: Degree, major, institution, graduation year
- **Experience**: Work history, internships, projects
- **Skills**: Technical and soft skills, certifications
- **Preferences**: Ideal work environment, salary expectations, work-life balance preferences
- **Goals**: Career objectives, desired industries, location preferences

**How to conduct the assessment:**
1. Present the questionnaire to the user in a conversational format
2. Ask follow-up questions to clarify ambiguous responses
3. Document all responses in a structured format
4. Summarize key insights about the user's profile

### Step 2: Job Market Research
Search for relevant job opportunities based on the user's background and preferences:

**Search strategies:**
- Use web search tools to find current job openings
- Focus on platforms like LinkedIn, Indeed, company career pages
- Consider both full-time positions and internships
- Look for remote, hybrid, and on-site opportunities as per user preference

**Data collection:**
- Job title, company name, location
- Required qualifications and skills
- Salary range (when available)
- Application deadline
- Job description summary

**Output format:**
Create an Excel spreadsheet (`jobs.xlsx`) with the following columns:
- Job Title
- Company
- Location (City, State/Country)
- Job Type (Full-time, Part-time, Internship)
- Remote/Hybrid/On-site
- Required Experience
- Required Education
- Key Skills Required
- Salary Range
- Application Link
- Deadline
- Notes

### Step 3: Resume Generation
Create a personalized resume based on the user's background:

**Resume structure:**
1. **Contact Information**: Name, phone, email, LinkedIn profile, location
2. **Professional Summary**: 2-3 sentence overview highlighting key qualifications
3. **Work Experience**: Reverse chronological order with bullet points emphasizing achievements
4. **Education**: Degrees, institutions, graduation dates, relevant coursework
5. **Skills**: Categorized (Technical, Soft, Certifications)
6. **Projects/Portfolio**: Relevant academic or personal projects
7. **Additional Sections**: Languages, volunteer work, publications (if applicable)

**Customization tips:**
- Tailor resume to target job types identified in Step 2
- Use action verbs and quantify achievements where possible
- Match keywords from job descriptions
- Maintain professional formatting and consistency

## Templates and Resources

### Resume Templates
Use the templates in `assets/` directory as starting points:
- `resume_template_modern.md` - Clean, modern design
- `resume_template_traditional.md` - Conservative, professional layout
- `resume_template_creative.md` - For creative/design roles

### Questionnaire Template
Reference `references/questionnaire_guide.md` for comprehensive question sets and follow-up prompts.

### Excel Formatting
See `scripts/generate_excel.py` for automated Excel spreadsheet generation with proper formatting.

## Best Practices

1. **Privacy**: Never share user's personal information without explicit permission
2. **Accuracy**: Verify job postings are current and from legitimate sources
3. **Customization**: Tailor each resume to specific job applications
4. **Follow-up**: Suggest application tracking and follow-up strategies
5. **Continuous improvement**: Encourage users to update their profiles as they gain new experiences

## Example User Requests

- "Help me find software engineering jobs in San Francisco"
- "I need a resume for marketing positions"
- "What career options match my background in biology?"
- "Find remote data analyst positions with Python experience"
- "Create a career plan for someone transitioning from teaching to tech"
