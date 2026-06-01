# Publish to GitHub

## 1. Create a GitHub Repository

Recommended repository name:

```text
genvis-ai-sdk-examples
```

Recommended description:

```text
OpenAI-compatible SDK examples for Genvis AI text, image, and video APIs.
```

## 2. Initialize Git

```bash
git init
git add .
git commit -m "Initial Genvis AI SDK examples"
```

## 3. Push with GitHub CLI

```bash
gh repo create genvis-ai-sdk-examples --public --source=. --remote=origin --push
```

## 4. Push with Git Remote

If the repository already exists:

```bash
git remote add origin git@github.com:YOUR_ORG/genvis-ai-sdk-examples.git
git branch -M main
git push -u origin main
```

## 5. After Publishing

- Add the GitHub link to the website API docs.
- Pin the repository on the GitHub organization profile.
- Add topics: `openai-compatible`, `ai-api`, `image-generation`, `video-generation`, `genvis-ai`.
- Keep examples aligned with currently available models and pricing.
