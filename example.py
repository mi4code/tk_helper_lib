from tk_helper_lib import *

var1="one line"

tk_init("My window", "500x500", resizable=True)

tk_label("Hello world!")
tk_entry_text("Text:", "var1")
tk_entry_text_multiline("More text:", "var2")
tk_entry_file("File (doubleclick to open)", "file")
tk_entry_dir("Directory (doubleclick to open)", "dir")
tk_button("OK", "print('ok')")
tk_buttons2("Yes", "No", "print('yes')", "print('no')")

tk_handle()

print(var1.get(),var2.get(),file.get(),dir.get())