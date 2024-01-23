import esks

# 1. Studenci, którzy wskazali dorm i segment
# 2. Studenci, dla których istnieje dokładny typ segmentu
# 3. Studenci, dla których istnieje strictly better typ segmentu
# 4. jak 2, ale tam gdzie location nie odpowiada dorm
# 5. analogicznie do 4 dla 3
# 6. najbardziej zbliżony segment
#   dorm >> num_segment >> num_room >> condition >> bathroom >> kitchen >> ad

if __name__ == '__main__':
    esks.esks()
