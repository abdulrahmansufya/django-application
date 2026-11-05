from ..client import content_client
from ...models import Post


class PostNotFoundError(ValueError):
    """Raised when the requested post does not exist."""


def _build_summarization_prompt(content):
    return f"""
Summarize the following blog post.

Requirements:
- Keep the summary clear and concise.
- Include only the main ideas and important information.
- Do not add information that is not in the original post.
- The summary must not exceed 500 characters.

Blog post:
{content}
"""


def summarize_post(post_id):

    try:
        post_id = int(post_id)
    except (ValueError, TypeError):
        raise ValueError("Post ID must be a valid integer.")

    if post_id <= 0:
        raise ValueError("Post ID must be greater than zero.")

    try:
        post = Post.objects.get(title_id=post_id)
    except Post.DoesNotExist:
        raise PostNotFoundError(
            f"Post with ID {post_id} was not found."
        )

    if not post.content or not post.content.strip():
        raise ValueError("Post content cannot be empty.")

    prompt = _build_summarization_prompt(post.content.strip())

    summary = content_client.generate(prompt)

    if not summary or not summary.strip():
        raise ValueError("Generated summary is empty.")

    summary = summary.strip()

    if len(summary) > 500:
        summary = summary[:500].rsplit(" ", 1)[0].rstrip()

    return {
        "post_id": post.title_id,
        "title": post.title,
        "summary": summary,
        "length": len(summary)
    }