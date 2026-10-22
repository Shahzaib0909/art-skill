# Install Art Skill

Choose your platform below. Menu names and availability can differ by account, workspace settings, and app version. These steps were checked against official documentation on 22 October 2026; installation was not tested in every product.

## 1. Download and prepare

1. Open [Shahzaib0909/art-skill](https://github.com/Shahzaib0909/art-skill).
2. Select **Code > Download ZIP** and extract it.
3. Rename the extracted `art-skill-main` folder to `art-skill`.
4. Check that `art-skill/SKILL.md` and `art-skill/references/` exist. Keep the whole folder together.
5. For an upload that requires a ZIP, compress this renamed folder as `art-skill.zip`. On Windows, right-click the folder and choose **Compress to ZIP file** (or **Send to > Compressed (zipped) folder**). On macOS, right-click and choose **Compress**.

Expected package:

```text
art-skill.zip
└── art-skill/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── formats.md
        ├── project-records.md
        └── quality.md
```

Avoid a duplicate wrapper such as `art-skill/art-skill/SKILL.md`. Upload the complete package, not just `SKILL.md`, so its supporting guides remain available.

## 2. ChatGPT

Where your account supports custom skill uploads:

1. Open **Plugins** in the sidebar, then the **Skills** tab; some desktop layouts show **Skills** directly.
2. Select **Create > Upload from your computer**.
3. Select the prepared skill package and complete the import prompts.
4. Wait for the skill scan/review and finish installation if prompted.
5. Start a chat, type `@`, and select Art Skill when available, or ask: **Use Art Skill to create one poster from this brief.**

If Skills or upload is missing, check workspace permissions and product eligibility; attaching a ZIP to an ordinary chat is not the same as installing it. A local desktop route is described in the Codex section below.

Sources: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), [Build skills](https://learn.chatgpt.com/docs/build-skills).

## 3. Claude web, desktop, and Cowork

1. On individual accounts, open **Settings > Capabilities** and enable **Code execution and file creation**. Organization accounts may require an administrator to enable skills.
2. Open **Customize > Skills**.
3. Select **+ > Create skill > Upload a skill**.
4. Upload `art-skill.zip` and turn the skill on.
5. Start a new chat or Cowork task and ask: **Use Art Skill to create a five-slide carousel about my service.**

If upload fails, check the folder name, required `SKILL.md`, ZIP nesting, and account permissions. Installing the workflow does not add an image model; use available tools or request a production specification when artwork cannot be rendered.

Source: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## 4. Gemini Apps

1. Open [Gemini](https://gemini.google.com) on a computer.
2. Open **Customize > Skills**; if needed, open **More** first.
3. Select **Create > Upload**.
4. Choose the prepared folder or ZIP containing `SKILL.md` and the supporting files.
5. Review the imported skill, select **Create**, and check it is active.
6. In a chat/task, select Art Skill using `/` or `@`, depending on the interface, or ask Gemini to use it by name.

If Skills is unavailable, use the CLI route below if you have Gemini CLI. Updating reference files in the app requires uploading the full skill again.

Source: [Create and manage skills for Gemini Apps](https://support.google.com/gemini/answer/17094296?hl=en).

## 5. Claude Code

For personal use, put the complete folder at:

```text
~/.claude/skills/art-skill/SKILL.md
```

For a single project, use:

```text
<your-project>/.claude/skills/art-skill/SKILL.md
```

Keep `references/` alongside `SKILL.md`. Start Claude Code in the intended project and invoke:

```text
/art-skill Create one thumbnail using my supplied brief and portrait.
```

Source: [Claude Code skills](https://code.claude.com/docs/en/skills).

## 6. Gemini CLI

With Gemini CLI already installed, run:

```sh
gemini skills install https://github.com/Shahzaib0909/art-skill.git
```

Review and respond to the installation confirmation. In a running Gemini CLI session, refresh and check discovery:

```text
/skills reload
/skills list
```

Then ask: **Use art-skill to create one campaign poster from this brief.** Approve activation when prompted. You can also place the complete folder in `~/.gemini/skills/art-skill/` for personal use.

Source: [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/).

## 7. Codex and local desktop workflows

Ask the built-in installer:

```text
$skill-installer Install the skill from https://github.com/Shahzaib0909/art-skill
```

For a manual project installation, copy the folder into:

```text
<your-project>/.agents/skills/art-skill/
```

Open the project and select the skill with `$` or `/skills`; invoke it as `$art-skill`. Restart the app/session if it does not appear. For user-wide placement, follow the current local skill directory documented for your installation rather than assuming a cloud chat shares your local files.

Source: [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Check that installation worked

Send this small test with a poster attached:

```text
Use Art Skill. Correct only the spelling in this supplied poster.
Preserve the rest of the composition. Tell me if an editing tool is unavailable.
```

Confirm the skill is discoverable, its supporting files load, and the response respects the limited edit. If no artwork is attached, the assistant should request the asset rather than claim to have edited it.

For finished artwork, your platform must expose appropriate generation, editing, or layout tools. This package supplies design guidance; it does not supply model access, a subscription, or provider credits.
