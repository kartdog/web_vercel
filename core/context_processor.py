
"""
def total_carro(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})
        for key, value in carro.items():
            total += int(value.get("acumulado", 0))
    return {"total_carro": total}
"""

def total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if "carro" in request.session.keys():
            for key, value in request.session["carro"].items():
                total += int(value["acumulado"])
    return {"total_carro": total}