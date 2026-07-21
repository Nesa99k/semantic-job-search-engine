from src.models.job import Job
from src.models.document import Document
from typing import Any


class DocumentBuilder:
    """Convert a Job object into a Document object."""

# -------------------  build ------------------------------------

    def build(self, job: Job) -> Document:
        content = self._build_content(job)
        metadata = self._build_metadata(job)

        document = Document(
            content=content,
            metadata=metadata
        )
        return document

# -------------------  _build_content ----------------------------

    def _build_content(self, job: Job) -> str:

        lines = []

        lines.append(f"Job Title: {job.title}")

        lines.append(f"Category: {job.category}")

        lines.append(f"Industry: {job.industry}")

        lines.append(f"Location: {job.city}, {job.country}")

        lines.append(f"Experience Level: {job.experience_level}")

        lines.append(f"Years of Experience: {job.years_of_experience}")

        lines.append(f"Education: {job.education}")

        lines.append(f"Salary: ${job.salary:,.0f}")

        lines.append(f"Remote Work: {job.remote_work}")

        lines.append(
            f"Required Skills: {', '.join(job.skills)}"
        )

        lines.append(f"Demand Score: {job.demand_score:.2f}")

        return "\n".join(lines)

# ------------------- _build_metadata ----------------------------

    def _build_metadata(self, job: Job) -> dict[str, Any]:
        return {
            "job_id": job.job_id,

            "title": job.title,

            "category": job.category,

            "city": job.city,

            "country": job.country,

            "experience_level": job.experience_level,

            "salary": job.salary,

            "industry": job.industry,

            "remote_work": job.remote_work,

            "is_llm_role": job.is_llm_role,

            "is_remote_friendly": job.is_remote_friendly,

            "is_senior": job.is_senior,

            "posting_year": job.posting_year,

            "posting_month": job.posting_month
        }
