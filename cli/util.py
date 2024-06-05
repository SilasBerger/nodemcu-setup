import serial.tools.list_ports


COM_PORT_PREFIXES = ["cu.usb", "tty.usb"]


def list_port_candidates():
    def matches_any_prefix(port):
        return len([prefix for prefix in COM_PORT_PREFIXES if port.name.lower().startswith(prefix)]) > 0

    ports = serial.tools.list_ports.comports()
    return [candidate.device for candidate in filter(matches_any_prefix, ports)]


def determine_unique_port_or_fail():
    port_candidates = list_port_candidates()
    if len(port_candidates) > 1:
        raise "Unable to identify unique port. Candidates are: " + ", ".join(port_candidates)
    if len(port_candidates) == 0:
        raise "No suitable port found for prefixes: " + ", ".join(COM_PORT_PREFIXES)
    return port_candidates[0]
