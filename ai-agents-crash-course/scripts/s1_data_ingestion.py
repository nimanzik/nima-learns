import io
import zipfile

import frontmatter
import requests


def read_repo_markdown_files(repo_owner: str, repo_name: str, branch: str = "main")-> list:
    """Read Markdown and React Markdown files (.md and .mdx) from a GitHub repository."""
    zip_url = f"https://codeload.github.com/{repo_owner}/{repo_name}/zip/refs/heads/{branch}"
    response = requests.get(zip_url)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        raise RuntimeError(f"Failed to download repository: {e}")

    extracted_data = []
    with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
        for file_info in zf.infolist():

            if not file_info.filename.lower().endswith((".md", ".mdx")):
                continue

            with zf.open(file_info) as file:
                content = file.read().decode("utf-8", errors="ignore")

                post = frontmatter.loads(content)
                data = post.to_dict()
                data["filename"] = file_info.filename
                extracted_data.append(data)

    return extracted_data


if __name__ == "__main__":
    dtc_faq = read_repo_markdown_files("DataTalksClub", "faq")
    print(f"FAQ documents: {len(dtc_faq)}")

    evidently_docs = read_repo_markdown_files("evidentlyai", "docs", branch="main")
    print(f"Evidently docs: {len(evidently_docs)}")
