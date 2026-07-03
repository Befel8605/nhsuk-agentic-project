"""Content health scanner for markdown files.

Scans all markdown files in the repository and generates a health report
covering documentation page count, broken links, and missing sections.
"""

import re
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

# Sections commonly expected in documentation files
EXPECTED_SECTIONS = ["## Overview", "## Usage", "## Contributing"]


def find_markdown_files(root: Path) -> list[Path]:
    """Return all markdown files in the repository, excluding hidden dirs."""
    return sorted(
        p for p in root.rglob("*.md")
        if not any(part.startswith(".") for part in p.relative_to(root).parts)
    )


def extract_links(content: str) -> list[str]:
    """Extract markdown links from content."""
    return re.findall(r"\[.*?\]\((.*?)\)", content)


def check_broken_links(md_file: Path, links: list[str]) -> list[str]:
    """Check for broken relative links (files that don't exist)."""
    broken = []
    for link in links:
        # Skip external URLs and anchors
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        # Resolve relative to the file's directory
        target = (md_file.parent / link).resolve()
        if not target.exists():
            broken.append(link)
    return broken


def check_missing_sections(content: str) -> list[str]:
    """Check which expected sections are missing from the content."""
    return [s for s in EXPECTED_SECTIONS if s.lower() not in content.lower()]


def generate_report() -> str:
    """Scan markdown files and generate the content health report."""
    md_files = find_markdown_files(REPO_ROOT)
    total_files = len(md_files)

    all_broken_links: dict[str, list[str]] = {}
    all_missing_sections: dict[str, list[str]] = {}

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8", errors="replace")
        rel_path = str(md_file.relative_to(REPO_ROOT))

        # Check broken links
        links = extract_links(content)
        broken = check_broken_links(md_file, links)
        if broken:
            all_broken_links[rel_path] = broken

        # Check missing sections
        missing = check_missing_sections(content)
        if missing:
            all_missing_sections[rel_path] = missing

    broken_link_count = sum(len(v) for v in all_broken_links.values())
    missing_section_count = sum(len(v) for v in all_missing_sections.values())
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Content Health Report",
        "",
        "## Summary",
        "",
        f"- **Documentation pages scanned:** {total_files}",
        f"- **Broken links found:** {broken_link_count}",
        f"- **Missing sections found:** {missing_section_count}",
        f"- **Last updated:** {now}",
        "",
    ]

    # Broken links details
    lines.append("## Broken Links")
    lines.append("")
    if all_broken_links:
        for file_path, broken in all_broken_links.items():
            lines.append(f"### `{file_path}`")
            lines.append("")
            for link in broken:
                lines.append(f"- `{link}`")
            lines.append("")
    else:
        lines.append("No broken links detected. :white_check_mark:")
        lines.append("")

    # Missing sections details
    lines.append("## Missing Sections")
    lines.append("")
    if all_missing_sections:
        for file_path, missing in all_missing_sections.items():
            lines.append(f"### `{file_path}`")
            lines.append("")
            for section in missing:
                lines.append(f"- {section}")
            lines.append("")
    else:
        lines.append("All files contain expected sections. :white_check_mark:")
        lines.append("")

    # Recommendations
    lines.append("## Recommendations")
    lines.append("")
    if broken_link_count > 0:
        lines.append("- Fix broken links listed above")
    if missing_section_count > 0:
        lines.append("- Add missing sections to improve documentation consistency")
    if broken_link_count == 0 and missing_section_count == 0:
        lines.append("- Documentation is in good health!")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    report = generate_report()
    output_dir = REPO_ROOT / "reports"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "content-health-report.md"
    output_file.write_text(report, encoding="utf-8")
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
