from google import genai

PROMPT_TEMPLATE = """
Split the provided document into logical sections for a Q&A system.

Each section should be self-contained and focused on a specific topic or concept.

CRITICAL RULES:
1. ONLY use exact text from the document: copy text VERBATIM
2. DO NOT add explanations, introductions, summaries, or commentary
3. Do NOT add phrases like "This section covers..." or "The document explains..."

<DOCUMENT>
{document}
</DOCUMENT>

Output format should be:

## [Short descriptive title]

[Exact verbatim text from document]

---

## [Another short descriptive title]

[Another exact verbatim text from document]

---
... and so on.
"""


client = genai.Client()


def chunk_document(document: str, model: str = "gemini-2.5-flash-lite") -> list[str]:
    """Chunk a document into logical sections using a powerful LLM."""
    prompt = PROMPT_TEMPLATE.format(document=document)
    response = client.models.generate_content(model=model, contents=prompt)

    if not response.text:
        return []

    sections = response.text.split("---")
    results = []
    for section in sections:
        section = section.strip()
        if section:
            results.append(section)

    return results


if __name__ == "__main__":

    sample_document = """
Artificial Intelligence (AI) is a branch of computer science that aims to create
machines capable of intelligent behavior. It encompasses various subfields, including
machine learning (ML), natural language processing (NLP), and robotics. ML, a subset
of AI, focuses on developing algorithms that allow computers to learn from and make
predictions based on data. NLP enables machines to understand and interpret human
language, facilitating better human-computer interactions. Robotics involves the design
and construction of robots that can perform tasks autonomously or semi-autonomously. The
integration of these subfields has led to significant advancements in technology,
impacting various industries such as healthcare, finance, and transportation.
    """

    chunks = chunk_document(sample_document)
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}:\n{chunk}\n")
