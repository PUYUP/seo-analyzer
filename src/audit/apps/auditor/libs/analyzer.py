from seoanalyzer import analyze


def run(site: str):
    output = analyze(site, analyze_headings=True, analyze_extra_tags=True)

    return output
