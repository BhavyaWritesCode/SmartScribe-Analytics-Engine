def generate_dita_xml(structure: dict, topic_type: str = "task") -> str:
    """Convert structured content into DITA-style XML format."""

    title = structure.get("title", "Untitled")
    summary = structure.get("summary", "")
    steps = structure.get("steps", [])
    notes = structure.get("notes", "")

    if topic_type == "task":
        return _generate_task_xml(title, summary, steps, notes)
    elif topic_type == "concept":
        return _generate_concept_xml(title, summary, notes)
    elif topic_type == "reference":
        return _generate_reference_xml(title, summary, steps, notes)
    else:
        return _generate_task_xml(title, summary, steps, notes)


def _generate_task_xml(title, summary, steps, notes) -> str:
    steps_xml = "\n".join(
        f"        <step>\n            <cmd>{step}</cmd>\n        </step>"
        for step in steps
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd">
<task id="task_001">
    <title>{title}</title>
    <shortdesc>{summary}</shortdesc>
    <taskbody>
        <steps>
{steps_xml}
        </steps>
        <postreq>
            <note>{notes}</note>
        </postreq>
    </taskbody>
</task>"""


def _generate_concept_xml(title, summary, notes) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">
<concept id="concept_001">
    <title>{title}</title>
    <shortdesc>{summary}</shortdesc>
    <conbody>
        <p>{summary}</p>
        <note>{notes}</note>
    </conbody>
</concept>"""


def _generate_reference_xml(title, summary, steps, notes) -> str:
    items_xml = "\n".join(
        f"        <strow>\n            <stentry>{step}</stentry>\n        </strow>"
        for step in steps
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE reference PUBLIC "-//OASIS//DTD DITA Reference//EN" "reference.dtd">
<reference id="reference_001">
    <title>{title}</title>
    <shortdesc>{summary}</shortdesc>
    <refbody>
        <simpletable>
            <sthead>
                <stentry>Reference Items</stentry>
            </sthead>
{items_xml}
        </simpletable>
        <note>{notes}</note>
    </refbody>
</reference>"""