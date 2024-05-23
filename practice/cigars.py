def cigar_party(cigars, is_weekend):
    if is_weekend == False:
        if 40<=cigars<=60:
            return True
        else:
            return False
    else:
        if 40<=cigars:
            return True
        else:
            return False

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))