from openclaw import Claw

# Load model (mistral, llama, qwen etc.)
claw = Claw(model="mistral")

with open("tfplan_small.txt") as f:
    plan = f.read().strip()

plan = plan[:10000]

prompt = f"""
Analyze this Terraform plan and identify:

1. Security issues
2. Misconfigurations
3. Cost risks
4. Best practice violations

Terraform Plan:
{plan}
"""

# ✅ FIX HERE
response = claw.run(prompt)

print(response)
