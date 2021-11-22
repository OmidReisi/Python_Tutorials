def logger(msg):
    def log_message():
        print("Log", msg)

    return log_message


# this sets the msg for inner log_message function as "Hi!" and when this inner function gets returned it remembers that
log_hi = logger("Hi!")

log_hi()


def html_tag(tag_name):
    def wrap_text(msg):
        print(("<{0}>{1}</{0}>".format(tag_name, msg)))

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Test Heading")

print_p = html_tag("p")
print_p("Test Paragraph")
