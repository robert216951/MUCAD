def classify_action_type(action: str) -> int:
    # Creating-Part
    if action in ["Add part studio feature", "Copy paste sketch"]:
        return 0
    # Creating-Assembly
    if action in ["Add assembly feature", "Add assembly instance", "Linked document insert"] or ("Paste :" in action):
        return 1
    # Editing-Part
    elif action in ["Start edit of part studio feature"] or ("Move :" in action or "Move to origin :" in action):
        return 2
    # Editing-Assembly
    elif action in ["Start edit of assembly feature", "Set mate values", "Start assembly drag", "Load named position"] or (
            "Fix :" in action or "Unfix :" in action or "Replace :" in action or "Suppress :" in action or
            "Unsuppress :" in action or
            "Configure suppression state" in action):
        return 3
    # Editing-Non-geometry
    elif "Assign material :" in action or "Change part appearance :" in action:
        return 4
    # Deleting-Part
    elif action in ["Delete part studio feature"]:
        return 5
    # Deleting-Assembly
    elif action in ["Delete assembly feature", "Delete assembly instance"]:
        return 6
    # Reversing
    elif action in ["Cancel Operation", "Undo Redo Operation", "Reset mates to initial positions",
                    "Restore Document From History"]:
        return 7
    # Organizing-Design
    elif action in ["Copy workspace", "Branch Workspace", "Create version", "Change configuration", "Edit configuration table"] or (
            "Restructure :" in action or "Select context :" in action or "Update context :" in action) or ("Metadata" in action and "updated" in action):
        return 8
    # Organizing-Support design process
    elif action in ["Update document description", "Move document", "Change properties", "Comment on a Document"] or (
            "Tab" in action and (
            "created" in action or "deleted" in action or "renamed" in action or "moved" in action)) or (
            "Rename part :" in action or "Rename document :" in action or "Create new folder :" in action or "Change Description :" in action or "Change Vendor :" in action):
        return 9
        # Viewing
    elif action in ["Animate action called"] or (
                "Show :" in action or "Hide :" in action or "Use automatic tessellation setting :" in action or "Use best available tessellation :" in action):
        return 10
    # Not classified (Optional: print out the unclassified actions)
    else:
        #print(action)
        return -1
