from dataclasses import dataclass


@dataclass
class Job:
    """Represents a single AI job posting."""

    # ---------- Identity ----------
    job_id: str
    title: str
    category: str
    # ---------- Location ----------
    city: str
    country: str
    # ---------- Experience ----------
    experience_level: str
    years_of_experience: int
    education: str
    # ---------- Salary ----------
    salary: float
    salary_min: float
    salary_max: float
    salary_tier: str
    # ---------- Company ----------
    company_size: str
    industry: str
    # ---------- Skills ----------
    skills: list[str]
    # ---------- Market Metrics ----------
    salary_premium: float
    demand_score: float
    demand_growth: float
    benefits_score: float
    # ---------- Posting ----------
    posting_year: int
    posting_month: int
    # ---------- Flags ----------
    remote_work: str
    is_senior: bool
    is_remote_friendly: bool
    is_llm_role: bool

    # ---------- Summary method ----------
