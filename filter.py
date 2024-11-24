import pandas as pd

# Defining the job details based on your input
data = {
    'Sn': [1, 2, 3, 4, 5],
    'Skill': [
        'Carpenter', 
        'Electrician (Cabling Technician)', 
        'HELPER GCC', 
        'Mason Labour', 
        'Steel Fixture/Civil Mason'
    ],
    'Quality_men': [10, 10, 10, 10, 5],
    'Quality_female': [0, 0, 0, 0, 0],
    'Salary': [1200.00, 1200.00, 1000.00, 1200.00, 1200.00],
    'Fooding': [''] * 5,  # Assuming fooding information is missing
    'Accommodation': [''] * 5,  # Assuming accommodation information is missing
    'Duration': [2] * 5,
    'Service Charge': [0] * 5,
    'Total Fee': [0] * 5
}

# Company details
company_info = {
    'Recruiting Agency': 'SATYA SAI OVERSEAS PVT LTD',
    'Lt #': '311897',
    'Country': 'UAE',
    'Company': 'BENCHMARK STAR ELECTROMECHANICAL WORKS L.L.C',
    'Approved Date': '2024/10/06'
}

# Create a DataFrame for the job details
df_jobs = pd.DataFrame(data)

# Add the company information to each row
for key, value in company_info.items():
    df_jobs[key] = value

# Reorder columns so company information appears first
df_jobs = df_jobs[[
    'Recruiting Agency', 'Lt #', 'Country', 'Company', 'Approved Date',
    'Sn', 'Skill', 'Quality_men', 'Quality_female', 'Salary', 'Fooding', 
    'Accommodation', 'Duration', 'Service Charge', 'Total Fee'
]]

# Save to an Excel file
df_jobs.to_excel("satya_sai_overseas_details.xlsx", index=False)
print("Data has been saved to satya_sai_overseas_details.xlsx")
