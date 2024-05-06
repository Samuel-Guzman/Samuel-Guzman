class Resume:
    def __init__(self, name, contact_info, objective, experiences, skills, education, certifications, projects, references):
        self.name = name
        self.contact_info = contact_info
        self.objective = objective
        self.experiences = experiences
        self.skills = skills
        self.education = education
        self.certifications = certifications
        self.projects = projects
        self.references = references

    def generate_resume(self):
        resume = f"""
        Name: {self.name}
        Contact Information: {self.contact_info}

        Objective:
        {self.objective}

        Professional Experience:
        {self._format_experiences()}

        Skills:
        {', '.join(self.skills)}

        Education:
        {self.education}

        Certifications:
        {', '.join(self.certifications)}

        Projects:
        {self._format_projects()}

        References:
        {self.references}
        """
        return resume

    def _format_experiences(self):
        formatted_experiences = ""
        for idx, experience in enumerate(self.experiences, 1):
            formatted_experiences += f"{idx}. {experience}\n"
        return formatted_experiences

    def _format_projects(self):
        formatted_projects = ""
        for idx, project in enumerate(self.projects, 1):
            formatted_projects += f"{idx}. {project}\n"
        return formatted_projects


# Example data
name = "Samuel Guzman"
contact_info = "Phone: 623-556-6061\nEmail: Samuel.L.Guzman@Gmail.com"
objective = "A skilled risk manager seeking opportunities as a python developer with emphasis in cybersecurity and financial banking."
experiences = [
    "Senior mortgage underwriter at Discover Home Loans.", "Python Software Engineer at XYZ Inc. - Developed backend services for a large-scale e-commerce platform.",
]
skills = ["Python", "Cybersecurity", "Flask", "SQLAlchemy", "SQL", "Tableau", "Git/GitHub", "API Interaction"]
education = "Bachelor of Science Global Business Management with concentration in Financial Management"
certifications = ["Cybersecurity Certification from eCornell", "Data Analytics from The University of Arizona Office of Continuing & Professional Education"]
projects = ["https://github.com/Samuel-Guzman/Samuel-Guzman.git"]
references = "Available upon request"

# Create Resume instance
resume = Resume(name, contact_info, objective, experiences, skills, education, certifications, projects, references)

# Generate and print the resume
print(resume.generate_resume())
