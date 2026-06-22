from flask import Flask, render_template

app = Flask(__name__)

OVERVIEW = [
    {"label": "Current version", "value": "v1.0.0", "mono": True},
    {"label": "Build status", "value": "Success", "mono": False, "highlight": True},
    {"label": "Environment", "value": "Production", "mono": False},
    {"label": "Last deployment", "value": "Today, 14:02", "mono": False},
]

SERVICES = [
    {"name": "GitHub", "icon": "ti-brand-github"},
    {"name": "Jenkins", "icon": "ti-cube"},
    {"name": "Docker", "icon": "ti-brand-docker"},
    {"name": "Terraform", "icon": "ti-stack-2"},
    {"name": "ECS Fargate", "icon": "ti-brand-aws"},
]

PIPELINE = ["GitHub", "Jenkins", "Docker", "ECS Fargate"]

ARCHITECTURE = [
    {"icon": "ti-git-branch", "title": "Source control", "tool": "GitHub"},
    {"icon": "ti-refresh", "title": "Continuous integration", "tool": "Jenkins"},
    {"icon": "ti-box", "title": "Containerization", "tool": "Docker"},
    {"icon": "ti-server-2", "title": "Infrastructure as code", "tool": "Terraform"},
    {"icon": "ti-cloud", "title": "Cloud hosting", "tool": "AWS ECS Fargate"},
]

DEPLOY_FREQUENCY = [35, 55, 40, 75, 60, 30, 100]
DEPLOY_FREQUENCY_LABELS = ["M", "T", "W", "T", "F", "S", "S"]

UPTIME_POINTS = "0,22 80,24 160,14 240,19 320,9 400,12 480,6 560,8"
UPTIME_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

ACTIVITY = [
    {
        "status": "success",
        "text_html": 'Deployment <span class="mono accent">#214</span> succeeded to production',
        "meta": "today 14:02 · ecs-fargate · 8f3a1c2",
    },
    {
        "status": "success",
        "text_html": "Docker image built and pushed to ECR",
        "meta": "today 13:58 · jenkins build #482",
    },
    {
        "status": "neutral",
        "text_html": "Terraform plan applied, no infrastructure drift",
        "meta": "today 13:51 · staging",
    },
    {
        "status": "success",
        "text_html": 'Pull request <span class="mono accent">#89</span> merged to main',
        "meta": "today 13:45 · github",
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        overview=OVERVIEW,
        services=SERVICES,
        pipeline=PIPELINE,
        architecture=ARCHITECTURE,
        deploy_frequency=DEPLOY_FREQUENCY,
        deploy_frequency_labels=DEPLOY_FREQUENCY_LABELS,
        uptime_points=UPTIME_POINTS,
        uptime_days=UPTIME_DAYS,
        activity=ACTIVITY,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)