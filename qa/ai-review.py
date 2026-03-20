import subprocess

# Read the compact Terraform plan
with open("tfplan_small.txt") as f:
    plan = f.read().strip()

prompt = f"""
You are an expert DevOps and Cloud Security reviewer.

Analyze this Terraform plan and identify:

1. Security issues
2. Misconfigurations
3. Cost risks
4. Best practice violations

For each issue, include:
- Severity (Low/Medium/High/Critical)
- Resource name
- Explanation
- Suggested fix

Terraform Plan:
{plan}
"""

# Call OpenCLAW CLI
result = subprocess.run(
    ["openclaw", "run", "--model", "mistral", "--prompt", prompt],
    text=True,
    capture_output=True
)

# Print model output to Jenkins console
if result.stderr:
    print("OpenCLAW stderr:", result.stderr)

print(result.stdout)
