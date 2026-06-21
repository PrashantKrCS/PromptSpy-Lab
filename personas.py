import random

PERSONAS = [
    {
        "name": "Amit Sharma",
        "role": "Security Engineer",
        "interest": "OWASP"
    },
    {
        "name": "Priya Patel",
        "role": "Cloud Architect",
        "interest": "Azure"
    },
    {
        "name": "Rahul Mehta",
        "role": "Software Developer",
        "interest": "Artificial Intelligence"
    },
    {
        "name": "Sneha Desai",
        "role": "Threat Researcher",
        "interest": "Malware Analysis"
    },
    {
        "name": "Arjun Nair",
        "role": "DevOps Engineer",
        "interest": "Kubernetes"
    }
]

THEMES = [
    "Conference Materials",
    "Research Report",
    "Security Survey",
    "Training Portal",
    "Industry Webinar"
]

EMAIL_TEMPLATES = [
    """
Subject: Updated {theme}

Hi {name},

Based on your interest in {interest}, we thought you might find these
new resources useful.

This is a security awareness simulation.

Regards,
Research Team
""",
    """
Subject: New {theme} Available

Hello {name},

As a {role}, you may be interested in our latest material related to
{interest}.

This message is part of a training simulation.

Regards,
Awareness Team
""",
    """
Subject: {theme} Preview

Hi {name},

We've published new educational content that may be relevant to your
interest in {interest}.

No action is required. This is a simulated awareness exercise.

Regards,
Training Team
"""
]


def generate_persona():
    return random.choice(PERSONAS)


def generate_email(persona):
    template = random.choice(EMAIL_TEMPLATES)

    theme = random.choice(THEMES)

    return {
        "theme": theme,
        "email": template.format(
            name=persona["name"],
            role=persona["role"],
            interest=persona["interest"],
            theme=theme
        )
    }


if __name__ == "__main__":

    persona = generate_persona()

    campaign = generate_email(persona)

    print("Persona")
    print(persona)

    print("\nGenerated Email")
    print(campaign["email"])
