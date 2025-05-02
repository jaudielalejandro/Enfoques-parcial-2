base = {
    "llueve": True,
    "tengo_paraguas": False,
    "me_mojo": lambda llueve, paraguas: llueve and not paraguas
}

print("¿Me mojo?", base["me_mojo"](base["llueve"], base["tengo_paraguas"]))
