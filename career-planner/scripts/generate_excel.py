#!/usr/bin/env python3
"""
Excel Job List Generator for Career Planner Skill

This script creates formatted Excel spreadsheets from job search results.
"""

import pandas as pd
from datetime import datetime
import argparse
import json
import sys
from typing import List, Dict, Any
import os


def create_jobs_dataframe(jobs_data: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Create a pandas DataFrame from job data with standardized columns.
    
    Args:
        jobs_data: List of job dictionaries
        
    Returns:
        pandas DataFrame with formatted job data
    """
    # Define column order and data types
    columns = [
        'Job Title',
        'Company',
        'Location',
        'Job Type',
        'Work Arrangement',
        'Required Experience',
        'Required Education',
        'Key Skills Required',
        'Salary Range',
        'Application Link',
        'Deadline',
        'Date Found',
        'Notes'
    ]
    
    # Create DataFrame
    df = pd.DataFrame(jobs_data)
    
    # Ensure all columns exist (add missing ones with NaN)
    for col in columns:
        if col not in df.columns:
            df[col] = None
    
    # Reorder columns
    df = df[columns]
    
    # Format dates
    date_columns = ['Deadline', 'Date Found']
    for col in date_columns:
        if col in df.columns and df[col].notna().any():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except:
                pass
    
    return df


def apply_excel_formatting(writer: pd.ExcelWriter, df: pd.DataFrame):
    """
    Apply formatting to Excel worksheet.
    
    Args:
        writer: pandas ExcelWriter object
        df: DataFrame to format
    """
    workbook = writer.book
    worksheet = writer.sheets['Jobs']
    
    # Define formats
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#4F81BD',
        'font_color': 'white',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
    })
    
    date_format = workbook.add_format({
        'num_format': 'yyyy-mm-dd',
        'align': 'left'
    })
    
    url_format = workbook.add_format({
        'font_color': 'blue',
        'underline': 1
    })
    
    # Apply header formatting
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
    # Auto-adjust column widths
    for i, col in enumerate(df.columns):
        column_width = max(df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(i, i, min(column_width, 50))
    
    # Apply special formatting to specific columns
    if 'Application Link' in df.columns:
        app_link_idx = df.columns.get_loc('Application Link')
        for row_num in range(1, len(df) + 1):
            url = df.iloc[row_num - 1]['Application Link']
            if pd.notna(url) and isinstance(url, str):
                worksheet.write_url(row_num, app_link_idx, url, url_format, string=url[:50] + '...' if len(url) > 50 else url)
    
    if 'Deadline' in df.columns:
        deadline_idx = df.columns.get_loc('Deadline')
        worksheet.set_column(deadline_idx, deadline_idx, 12, date_format)
    
    if 'Date Found' in df.columns:
        date_found_idx = df.columns.get_loc('Date Found')
        worksheet.set_column(date_found_idx, date_found_idx, 12, date_format)
    
    # Add filters
    worksheet.autofilter(0, 0, len(df), len(df.columns) - 1)
    
    # Freeze header row
    worksheet.freeze_panes(1, 0)


def generate_jobs_excel(jobs_data: List[Dict[str, Any]], output_path: str = 'jobs.xlsx'):
    """
    Generate formatted Excel file from job data.
    
    Args:
        jobs_data: List of job dictionaries
        output_path: Path to save Excel file
    """
    if not jobs_data:
        print("No job data provided. Creating empty template.")
        # Create empty DataFrame with correct columns
        jobs_data = [{}]
    
    # Create DataFrame
    df = create_jobs_dataframe(jobs_data)
    
    # Create Excel writer
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        # Write data
        df.to_excel(writer, sheet_name='Jobs', index=False)
        
        # Apply formatting
        apply_excel_formatting(writer, df)
        
        # Add summary sheet
        summary_data = {
            'Metric': ['Total Jobs', 'Full-time Positions', 'Remote Opportunities', 
                      'With Salary Info', 'Upcoming Deadlines'],
            'Count': [
                len(df),
                len(df[df['Job Type'] == 'Full-time']),
                len(df[df['Work Arrangement'].str.contains('Remote', na=False)]),
                len(df[df['Salary Range'].notna()]),
                len(df[df['Deadline'].notna()])
            ]
        }
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        # Format summary sheet
        workbook = writer.book
        summary_ws = writer.sheets['Summary']
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#9BBB59',
            'font_color': 'white',
            'border': 1
        })
        
        for col_num, value in enumerate(summary_df.columns.values):
            summary_ws.write(0, col_num, value, header_format)
        
        summary_ws.set_column(0, 0, 25)
        summary_ws.set_column(1, 1, 15)
    
    print(f"Excel file created: {output_path}")
    print(f"Total jobs included: {len(df)}")


def load_json_data(json_path: str) -> List[Dict[str, Any]]:
    """
    Load job data from JSON file.
    
    Args:
        json_path: Path to JSON file
        
    Returns:
        List of job dictionaries
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, dict) and 'jobs' in data:
            return data['jobs']
        elif isinstance(data, list):
            return data
        else:
            print(f"Warning: Unexpected JSON structure in {json_path}")
            return []
    except FileNotFoundError:
        print(f"Error: JSON file not found: {json_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {json_path}: {e}")
        return []


def create_sample_data() -> List[Dict[str, Any]]:
    """
    Create sample job data for testing.
    
    Returns:
        List of sample job dictionaries
    """
    return [
        {
            'Job Title': 'Software Engineer',
            'Company': 'Tech Corp Inc.',
            'Location': 'San Francisco, CA',
            'Job Type': 'Full-time',
            'Work Arrangement': 'Hybrid',
            'Required Experience': '3+ years',
            'Required Education': 'Bachelor\'s in CS or related',
            'Key Skills Required': 'Python, JavaScript, React, AWS',
            'Salary Range': '$120,000 - $160,000',
            'Application Link': 'https://techcorp.com/careers/software-engineer',
            'Deadline': '2024-06-30',
            'Date Found': datetime.now().strftime('%Y-%m-%d'),
            'Notes': 'Fast-growing startup, good benefits'
        },
        {
            'Job Title': 'Data Analyst',
            'Company': 'Data Insights LLC',
            'Location': 'Remote',
            'Job Type': 'Full-time',
            'Work Arrangement': 'Remote',
            'Required Experience': '2+ years',
            'Required Education': 'Bachelor\'s degree',
            'Key Skills Required': 'SQL, Python, Tableau, Statistics',
            'Salary Range': '$85,000 - $110,000',
            'Application Link': 'https://datainsights.com/jobs/data-analyst',
            'Deadline': '2024-07-15',
            'Date Found': datetime.now().strftime('%Y-%m-%d'),
            'Notes': 'Fully remote, flexible hours'
        }
    ]


def main():
    parser = argparse.ArgumentParser(description='Generate Excel spreadsheet from job data')
    parser.add_argument('--input', '-i', type=str, help='Input JSON file with job data')
    parser.add_argument('--output', '-o', type=str, default='jobs.xlsx', help='Output Excel file path')
    parser.add_argument('--sample', '-s', action='store_true', help='Generate sample data for testing')
    
    args = parser.parse_args()
    
    if args.sample:
        print("Generating sample job data...")
        jobs_data = create_sample_data()
    elif args.input:
        jobs_data = load_json_data(args.input)
        if not jobs_data:
            print("No valid job data found. Exiting.")
            sys.exit(1)
    else:
        print("Please provide either --input JSON file or --sample flag")
        parser.print_help()
        sys.exit(1)
    
    # Generate Excel file
    generate_jobs_excel(jobs_data, args.output)


if __name__ == '__main__':
    main()