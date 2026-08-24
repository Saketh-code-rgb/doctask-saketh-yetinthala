**FIELD NOTES**

**SuperDocs Observations**

**What I tried**

1. Created a research-plan document for identifying open-source projects that use document manipulation libraries.
2. Used SuperDocs to modify an existing document through natural-language instructions.
3. Asked SuperDocs to update specific research questions while keeping other sections unchanged.
4. Asked SuperDocs to add a new Research Method section.
5. Used the AI-generated review workflow to review proposed document changes.
6. Accepted an AI-generated change through the review mode.
7. Asked SuperDocs to add research findings to the document.
8. Asked SuperDocs to add a new section containing library-usage information.
9. Tested document formatting using the editor toolbar, including:
   - Bold
   - Italic
   - Underline
   - Strikethrough
   - H1
   - H2
   - H3
10. Tested formatting when the cursor was placed inside or next to existing text without explicitly selecting the text.
11. Tested formatting after selecting a specific piece of text.
12. Observed the AI progress/waiting state while SuperDocs was processing changes.
13. Tested the review mode where AI-generated changes are shown before acceptance.
14. Accepted changes using the review interface.
15. Observed the document after accepting AI-generated changes.
16. Tested the document tab/navigation area at the top of the editor.
17. Tested the chat/conversation area and its controls.
18. Tested the "Generate an image" workflow and its modal dialog.
19. Tested the Cancel and Send controls in the image-generation modal.
20. Uploaded a PDF resume containing a visible watermark and asked SuperDocs to identify/search for the watermark.
21. Observed how SuperDocs responded when analyzing the uploaded PDF.
22. Observed SuperDocs' handling of the watermark even though the watermark was visibly present in the uploaded document.
23. Reviewed the overall editing experience, including AI responses, progress indicators, review mode, document formatting, and error/limitation messaging.

**What worked well**

- Natural-language document editing was easy to understand and required little manual formatting.
- SuperDocs was able to make meaningful changes to an existing document based on instructions.
- The review workflow provides a useful separation between an AI-proposed change and the final accepted document.
- The ability to accept or deny individual AI-generated changes gives the user control over document modifications.
- The AI provides progress information while working on larger document operations.
- The document editor provides familiar formatting controls similar to a traditional word processor.
- Research-oriented workflows can be performed directly inside the document.
- SuperDocs can add structured research findings and tables to a document.
- The system can work with uploaded documents as part of an AI workflow.
- The document editor provides a relatively clean interface with the conversation panel and document panel separated.
- Version/revert-related functionality provides useful protection against unwanted AI changes.
- The review mode makes it easier to understand that an AI operation has changed the document before accepting it.
- The ability to generate images from an AI instruction can be useful for reports and other documents.
- The system provides clear feedback when an operation is still being processed.

**What was confusing**

- It was not always clear how SuperDocs determines the exact text or paragraph to modify when the instruction could apply to multiple parts of the document.
- The difference between an AI-generated change, an accepted change, and a reverted change could be clearer to a new user.
- It is not always obvious what the AI is currently doing when a document operation takes a long time.
- Some AI responses indicate that the system is searching or processing a document, but the exact scope of the operation is not always clear.
- The formatting behavior is inconsistent depending on whether text is selected or only has the cursor positioned within it.
- It is unclear whether formatting controls are intended to operate on the current cursor position, the current paragraph, or explicitly selected text.
- The document tabs at the top do not visually balance the tab number and document name well.
- Some controls in the UI look clickable but do not have strong enough visual boundaries.
- The image-generation modal's Send button does not visually stand out as a conventional actionable button.
- The watermark/PDF limitation was confusing because the uploaded PDF visibly contained a watermark, while SuperDocs reported that it could not find one.

**What felt slow**

- Large document operations can take noticeable time before producing a result.
- The AI sometimes displays multiple progress messages while working on the same task.
- Research-related operations can take longer than simple document edits.
- Processing an uploaded PDF can take some time, particularly when SuperDocs is searching the document.
- It would be useful to have more precise progress information for long-running operations, such as the current processing stage and an estimated completion state.

**Bugs / errors / rough edges**

**1\. Inline formatting does not work consistently with cursor placement**

**Observed behavior:**

When the cursor is placed next to existing text, clicking Bold, Italic, or Underline does not behave as expected.

For example, with the cursor positioned at the end of:

_"potential need for AI-powered document editing solutions."_

clicking Bold/Italic/Underline does not apply the formatting to the intended existing sentence.

However, when the text is explicitly selected first, the formatting controls work.

**Expected behavior:**

The editor should clearly define the formatting behavior based on cursor position and selection. If the cursor is inside an existing text block, formatting should either apply to the current word/paragraph according to standard editor behavior or provide clear feedback about what will be formatted.

**2\. H1/H2/H3 formatting works without selecting the sentence**

**Observed behavior:**

When the cursor is placed next to the sentence:

_"potential need for AI-powered document editing solutions."_

clicking H1, H2, or H3 changes the size/style of the sentence even when the sentence has not been selected.

This behavior is different from the Bold/Italic/Underline behavior.

**Expected behavior:**

Formatting controls should have predictable and consistent behavior. The editor should clearly distinguish between:

- Character formatting
- Paragraph formatting
- Selection-based formatting
- Cursor-based formatting

**3\. Document tab number and document name are visually unbalanced**

**Observed behavior:**

The document tabs display a small tab number followed by the document name.

The number area is visually smaller than the document-name area, resulting in an uneven appearance.

Example: "1 Research Plan: Iden..."

The number and title do not appear visually balanced within the tab.

**Expected behavior:**

The tab number and document title should have consistent spacing, alignment, and sizing so the tab looks visually balanced.

**4\. Close/cross icon does not have a clear border**

**Observed behavior:**

In the conversation/input area, a small X/close icon is displayed on a UI element.

The icon does not have a clearly defined border or button boundary, making it look like plain text rather than an actionable control.

**Expected behavior:**

The close button should have a clear clickable area and consistent visual styling with other interactive controls.

**5\. "Send" button in Generate an Image modal lacks clear button styling**

**Observed behavior:**

The "Generate an image" modal contains a description input, a Cancel button, and a Send button.

The Cancel button has a visible border, while the Send button appears much less visually prominent and does not have the same clear button boundary.

**Expected behavior:**

The primary Send action should have a clear button style and visual hierarchy so users can immediately recognize it as the primary action.

**6\. Watermark detection/search issue in uploaded PDF**

**Observed behavior:**

I uploaded a resume PDF containing a clearly visible watermark.

The watermark was visibly present in the PDF, but SuperDocs responded that it searched the document and did not find a watermark.

The response also stated that watermark removal/editing was outside its current editing scope.

**Expected behavior:**

If the PDF contains a visually detectable watermark, SuperDocs should either detect and identify the watermark correctly, or clearly state that it cannot reliably inspect image-based/PDF-level watermarks before claiming that no watermark was found.

The current behavior can give the user incorrect confidence that the document does not contain a watermark.

**7\. AI response can incorrectly conclude that a visual element is absent**

The watermark case suggests a broader limitation.

The uploaded document visibly contained an element that was not identified by the AI.

This raises a concern about how SuperDocs handles image-based content, visual elements, watermarks, scanned PDFs, embedded graphics, and other non-text document elements.

The system should distinguish between "I searched the text/content and did not find it" and "I verified visually that the element is not present."

**8\. Review-mode inserted content can require additional manual inspection**

The review mode provides useful Accept/Deny controls, but larger inserted sections can require the user to scroll through the proposed change to understand the complete modification.

For large tables or sections, a more convenient preview/diff experience could make review easier.

**9\. AI-generated content can contain placeholders that require user verification**

In one generated research section, placeholders such as "Please fill: Project Name" and "Please fill: Accurate description..." appeared in the generated document.

This means AI-generated document content may sometimes look complete while still containing unresolved placeholders.

**Expected behavior:**

SuperDocs could detect unresolved placeholders before presenting the operation as complete or clearly highlight them as items requiring user attention.

**Interesting growth opportunities**

- Add a stronger document-diff experience showing exactly what changed before and after an AI operation.
- Allow users to compare two document versions side by side.
- Provide clearer progress stages for long-running AI operations.
- Allow users to cancel long-running operations safely.
- Provide a more powerful version-history interface.
- Allow users to restore individual changes instead of only reverting larger operations.
- Improve support for complex DOCX structures such as tables, images, headers, footers, comments, and tracked changes.
- Improve PDF understanding beyond text extraction.
- Add visual document inspection for watermarks, images, diagrams, and scanned content.
- Provide warnings when AI-generated content contains unresolved placeholders.
- Add a validation step before finalizing AI-generated reports.
- Provide stronger citation/source traceability for research-generated content.
- Allow users to export research findings separately from the final document.
- Provide reusable research workflows that can be repeated using the same criteria.
- Allow users to control how much autonomy the AI has when editing documents.
- Provide organization-level controls for document access, activity history, and auditing.
- Improve the consistency of editor controls so cursor-based and selection-based formatting behave predictably.
- Improve accessibility and visual affordances for small controls such as close, send, and tab controls.

**Features I think are especially valuable**

- Natural-language document editing.
- AI-assisted research and document generation.
- Review mode with Accept/Deny controls.
- Revert/version functionality.
- Live progress updates during AI operations.
- Ability to work with uploaded documents.
- Structured research findings and tables.
- Document formatting controls.
- Image generation directly within the document workflow.
- Ability to combine research, editing, and document generation in one workflow.
- AI assistance without requiring the user to manually perform every document-editing operation.

**Questions I still have**

- How does SuperDocs decide which paragraph or section to modify when the user's instruction is ambiguous?
- Why do Bold, Italic, and Underline behave differently when text is selected versus when only the cursor is positioned in the text?
- What is the intended behavior of formatting controls when no text is selected?
- Why do H1/H2/H3 change the current sentence/paragraph when only the cursor is positioned there?
- Are formatting controls character-level or paragraph-level operations?
- How are document versions stored and how long are previous versions retained?
- Can users compare two versions of a document side by side?
- Can users revert one accepted AI change without reverting other accepted changes?
- How does version history interact with the review/acceptance workflow?
- What happens if an AI-generated operation fails halfway through a document update?
- Is there an automatic recovery mechanism for failed document edits?
- Is there a reliable way to cancel a long-running AI operation?
- How does SuperDocs handle very large DOCX files?
- Are tables, images, headers, footers, and complex Word formatting preserved during AI edits?
- How does SuperDocs handle documents containing tracked changes or comments?
- Can the AI make changes across multiple sections while preserving formatting?
- How does SuperDocs validate AI-generated content before inserting it into a document?
- Can SuperDocs detect unresolved placeholders such as "Please fill: Project Name"?
- Are all AI-generated factual claims automatically sourced?
- How are citations generated and maintained when content is edited?
- Can users see the original source behind a research finding?
- Can research results be exported separately from the document?
- Can the same research workflow be repeated automatically using the same criteria?
- How does SuperDocs distinguish between text extraction and visual document understanding?
- Why was the visible watermark in the uploaded PDF not detected?
- Can SuperDocs reliably detect watermarks embedded as images in PDFs?
- Does SuperDocs support visual inspection of scanned PDFs?
- How does SuperDocs handle embedded images, diagrams, watermarks, and other non-text elements?
- When SuperDocs says an element was not found, does that mean it searched the text layer only or the complete visual document?
- Are there known limitations when analyzing PDFs compared with DOCX files?
- How does SuperDocs handle privacy and sensitive documents uploaded by users?
- Are uploaded documents used for model training?
- How long are uploaded documents and generated content retained?
- Can organizations apply access controls and audit logs for document activity?
- Are there limits on document size, AI requests, research operations, or image generation?
- Can users control the amount of autonomy given to the AI?
- How does SuperDocs handle conflicting edits when multiple changes are generated?
- How does SuperDocs handle errors when AI-generated content does not match the user's requested format?
- Can users customize how review changes are displayed for large document modifications?
- Can organizations define policies for AI-generated document changes and approvals?