automarkas = [
    "AUDI", "BMW", "MERCEDES-BENZ", "VOLKSWAGEN", "TOYOTA",
    "HONDA", "FORD", "CHEVROLET", "HYUNDAI", "NISSAN",
    "VOLVO", "KIA", "SUBARU", "MAZDA", "LEXUS"
]

def atrast_auto(marka, gads, ak, degviela, tilpums):

    automobili = [
        {"marka": "Audi", "modelis": "A1", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.0, 1.2, 1.4, 1.6, 2.0], "gadi": list(range(2010, 2024))},
        {"marka": "Audi", "modelis": "A3", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.2, 1.4, 1.6, 2.0, 3.0], "gadi": list(range(2000, 2024))},
        {"marka": "Audi", "modelis": "A4", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.4, 1.6, 2.0, 2.5, 3.0, 4.0], "gadi": list(range(2000, 2024))},
        {"marka": "Audi", "modelis": "A5", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.8, 2.0, 2.5, 3.0, 3.5], "gadi": list(range(2007, 2024))},
        {"marka": "Audi", "modelis": "A6", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 2.5, 3.0, 3.5, 4.0, 5.0], "gadi": list(range(2004, 2024))},
        {"marka": "Audi", "modelis": "A7", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [3.0, 4.0, 5.0], "gadi": list(range(2010, 2024))},
        {"marka": "Audi", "modelis": "A8", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [3.0, 4.0, 5.0, 6.0, 8.0], "gadi": list(range(2002, 2024))},
        {"marka": "Audi", "modelis": "Q3", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.4, 1.6, 2.0, 2.5], "gadi": list(range(2011, 2024))},
        {"marka": "Audi", "modelis": "Q5", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 2.5, 3.0, 3.5], "gadi": list(range(2008, 2024))},
        {"marka": "Audi", "modelis": "Q7", "ak": ["Manuālā", "Automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [3.0, 4.0, 5.0], "gadi": list(range(2005, 2024))},
        {"marka": "BMW", "modelis": "1 sērija", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.4, 1.6, 2.0, 2.5, 3.0], "gadi": list(range(2004, 2024))},
        {"marka": "BMW", "modelis": "2 sērija", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 1.6, 2.0, 2.5, 3.0], "gadi": list(range(2014, 2024))},
        {"marka": "BMW", "modelis": "3 sērija", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.6, 2.0, 2.5, 3.0, 3.5, 4.0], "gadi": list(range(2000, 2024))},
        {"marka": "BMW", "modelis": "4 sērija", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.5, 3.0, 3.5, 4.0], "gadi": list(range(2007, 2024))},
        {"marka": "BMW", "modelis": "5 sērija", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.5, 3.0, 3.5, 4.0, 5.0], "gadi": list(range(2003, 2024))},
        {"marka": "BMW", "modelis": "6 sērija", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 3.0, 4.0, 5.0], "gadi": list(range(2003, 2024))},
        {"marka": "BMW", "modelis": "7 sērija", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 5.0, 6.0, 8.0], "gadi": list(range(2002, 2024))},
        {"marka": "BMW", "modelis": "X1", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 1.6, 2.0, 2.5], "gadi": list(range(2009, 2024))},
        {"marka": "BMW", "modelis": "X3", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.5, 3.0, 3.5], "gadi": list(range(2003, 2024))},
        {"marka": "BMW", "modelis": "X4", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 3.0, 4.0], "gadi": list(range(2014, 2024))},
        {"marka": "BMW", "modelis": "X5", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 5.0], "gadi": list(range(2007, 2024))},
        {"marka": "BMW", "modelis": "X6", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 5.0], "gadi": list(range(2008, 2024))},
        {"marka": "BMW", "modelis": "X7", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 5.0], "gadi": list(range(2015, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "A klase", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.4, 1.6, 2.0], "gadi": list(range(2012, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "B klase", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 1.6, 2.0], "gadi": list(range(2011, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "C klase", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.6, 2.0, 2.5, 3.0, 3.5, 4.0], "gadi": list(range(2000, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "E klase", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.5, 3.0, 3.5, 4.0, 5.0], "gadi": list(range(2003, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "S klase", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 5.0, 6.0, 8.0], "gadi": list(range(2002, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "CLS", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 3.0, 4.0, 5.0], "gadi": list(range(2004, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "GLA", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 1.6, 2.0], "gadi": list(range(2013, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "GLC", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.5, 3.0], "gadi": list(range(2015, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "GLE", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 5.0], "gadi": list(range(2015, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "GLS", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 5.0], "gadi": list(range(2015, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "AMG GT", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [4.0, 4.5], "gadi": list(range(2014, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "AMG GT 4-Door Coupé", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [4.0, 4.5], "gadi": list(range(2018, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "AMG GT Roadster", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [4.0, 4.5], "gadi": list(range(2016, 2024))},
        {"marka": "Mercedes-Benz", "modelis": "AMG GT Cabriolet", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [4.0, 4.5], "gadi": list(range(2016, 2024))},
        {"marka": "Volkswagen", "modelis": "Golf", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.2, 1.4, 1.6, 2.0, 2.5, 3.0], "gadi": list(range(1974, 2024))},
        {"marka": "Volkswagen", "modelis": "Polo", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.0, 1.2, 1.4, 1.6], "gadi": list(range(1975, 2023))},
        {"marka": "Volkswagen", "modelis": "Passat", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.6, 2.0, 2.5, 3.0, 3.5, 4.0], "gadi": list(range(1973, 2024))},
        {"marka": "Volkswagen", "modelis": "Passat Variant", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 1.6, 2.0, 2.5, 3.0, 3.5], "gadi": list(range(2010, 2024))},
        {"marka": "Volkswagen", "modelis": "Sharan", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.9, 2.0, 2.5, 2.8, 3.0], "gadi": list(range(1995, 2024))},
        {"marka": "Volkswagen", "modelis": "Touareg", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [3.0, 4.0, 4.2, 5.0, 6.0, 8.0], "gadi": list(range(2002, 2024))},
        {"marka": "Volkswagen", "modelis": "Caddy", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.5, 3.0], "gadi": list(range(2003, 2024))},
        {"marka": "Volkswagen", "modelis": "Transporter", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.5, 3.0], "gadi": list(range(1950, 2024))},
        {"marka": "Toyota", "modelis": "Corolla", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.2, 1.4, 1.6, 2.0], "gadi": list(range(1966, 2024))},
        {"marka": "Toyota", "modelis": "Yaris", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.0, 1.2, 1.5], "gadi": list(range(1999, 2024))},
        {"marka": "Toyota", "modelis": "C-HR", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "hibrīds"], "tilpums": [1.8, 2.0], "gadi": list(range(2016, 2024))},
        {"marka": "Toyota", "modelis": "RAV4", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "hibrīds"], "tilpums": [2.0, 2.5, 3.5], "gadi": list(range(1994, 2024))},
        {"marka": "Toyota", "modelis": "Highlander", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "hibrīds"], "tilpums": [2.7, 3.5, 4.0], "gadi": list(range(2001, 2024))},
        {"marka": "Toyota", "modelis": "Land Cruiser", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.7, 3.5, 4.0, 5.7], "gadi": list(range(1951, 2024))},
        {"marka": "Toyota", "modelis": "Supra", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [3.0], "gadi": list(range(2019, 2023))},
        {"marka": "Toyota", "modelis": "GR Yaris", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [1.6], "gadi": list(range(2020, 2024))},
        {"marka": "Honda", "modelis": "Civic", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 2.0], "gadi": list(range(1972, 2024))},
        {"marka": "Honda", "modelis": "Jazz", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.2, 1.5], "gadi": list(range(2001, 2024))},
        {"marka": "Honda", "modelis": "CR-V", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 2.0, 2.5], "gadi": list(range(1995, 2024))},
        {"marka": "Honda", "modelis": "HR-V", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [1.5, 2.0], "gadi": list(range(2015, 2024))},
        {"marka": "Honda", "modelis": "Accord", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "dīzelis"], "tilpums": [2.0, 2.4, 3.0], "gadi": list(range(1976, 2024))},
        {"marka": "Honda", "modelis": "Odyssey", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.4, 3.5], "gadi": list(range(1994, 2024))},
        {"marka": "Honda", "modelis": "Pilot", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [3.5, 3.0], "gadi": list(range(2002, 2024))},
        {"marka": "Honda", "modelis": "Ridgeline", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [3.5], "gadi": list(range(2005, 2024))},
        {"marka": "Honda", "modelis": "Civic Type R", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [2.0], "gadi": list(range(2017, 2024))},
        {"marka": "Ford", "modelis": "Fiesta", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.1, 1.2, 1.5, 1.9], "gadi": list(range(1976, 2024))},
        {"marka": "Ford", "modelis": "Focus", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.1, 1.2, 1.5, 2.0], "gadi": list(range(1998, 2024))},
        {"marka": "Ford", "modelis": "Puma", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.5], "gadi": list(range(2019, 2024))},
        {"marka": "Ford", "modelis": "Kuga", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.5, 2.0, 2.5], "gadi": list(range(2008, 2024))},
        {"marka": "Ford", "modelis": "Escape", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 2.5], "gadi": list(range(2000, 2024))},
        {"marka": "Ford", "modelis": "EcoSport", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.5], "gadi": list(range(2012, 2024))},
        {"marka": "Ford", "modelis": "Edge", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 2.7, 3.5, 3.0], "gadi": list(range(2006, 2024))},
        {"marka": "Ford", "modelis": "Explorer", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 2.3, 3.0, 3.5, 5.0], "gadi": list(range(1990, 2024))},
        {"marka": "Ford", "modelis": "F-150", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.7, 3.0, 3.3, 3.5, 5.0, 5.2, 5.5, 7.3], "gadi": list(range(1948, 2024))},
        {"marka": "Ford", "modelis": "Ranger", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.3, 2.5, 3.2, 3.0], "gadi": list(range(1983, 2024))},
        {"marka": "Ford", "modelis": "Mustang", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.3, 5.0], "gadi": list(range(1964, 2024))},
        {"marka": "Ford", "modelis": "Focus ST", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [2.0], "gadi": list(range(2012, 2024))},
        {"marka": "Ford", "modelis": "Fiesta ST", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [1.5], "gadi": list(range(2013, 2024))},
        {"marka": "Ford", "modelis": "KA", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [1.3], "gadi": list(range(1996, 2022))},
        {"marka": "Chevrolet", "modelis": "Spark", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.4], "gadi": list(range(2009, 2023))},
        {"marka": "Chevrolet", "modelis": "Aveo", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.2, 1.6], "gadi": list(range(2002, 2023))},
        {"marka": "Chevrolet", "modelis": "Onix", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.4], "gadi": list(range(2012, 2023))},
        {"marka": "Chevrolet", "modelis": "Cobalt", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.2, 1.4], "gadi": list(range(2005, 2023))},
        {"marka": "Chevrolet", "modelis": "Tracker", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.0, 1.4], "gadi": list(range(2013, 2023))},
        {"marka": "Chevrolet", "modelis": "Trax", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.0, 1.4], "gadi": list(range(2013, 2023))},
        {"marka": "Chevrolet", "modelis": "Equinox", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.5, 2.0], "gadi": list(range(2004, 2023))},
        {"marka": "Chevrolet", "modelis": "Blazer", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.5, 3.6], "gadi": list(range(2019, 2023))},
        {"marka": "Chevrolet", "modelis": "Camaro", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 6.2], "gadi": list(range(1967, 2023))},
        {"marka": "Chevrolet", "modelis": "Corvette", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [6.2], "gadi": list(range(1953, 2023))},
        {"marka": "Chevrolet", "modelis": "Tahoe", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [5.3, 6.2], "gadi": list(range(1995, 2023))},
        {"marka": "Chevrolet", "modelis": "Suburban", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [5.3, 6.2], "gadi": list(range(1935, 2023))},
        {"marka": "Chevrolet", "modelis": "Silverado 1500", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.7, 6.6], "gadi": list(range(1999, 2023))},
        {"marka": "Chevrolet", "modelis": "Silverado 2500", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [6.0, 6.6], "gadi": list(range(1999, 2023))},
        {"marka": "Chevrolet", "modelis": "Silverado 3500", "ak": ["Manuālā", "automātiskā"], "degviela": ["Dīzelis"], "tilpums": [6.6], "gadi": list(range(1999, 2023))},
        {"marka": "Chevrolet", "modelis": "Colorado", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.5, 3.6], "gadi": list(range(2004, 2023))},
        {"marka": "Chevrolet", "modelis": "Canyon", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.5, 3.6], "gadi": list(range(2004, 2023))},
        {"marka": "Hyundai", "modelis": "Accent", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.1, 1.6], "gadi": list(range(2000, 2024))},
        {"marka": "Hyundai", "modelis": "Atos", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [0.8, 1.1], "gadi": list(range(2001, 2015))},
        {"marka": "Hyundai", "modelis": "Elantra", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.4, 2.0], "gadi": list(range(1990, 2024))},
        {"marka": "Hyundai", "modelis": "Getz", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.1, 1.6], "gadi": list(range(2002, 2012))},
        {"marka": "Hyundai", "modelis": "i10", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.2], "gadi": list(range(2007, 2024))},
        {"marka": "Hyundai", "modelis": "i20", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.0, 1.4], "gadi": list(range(2008, 2024))},
        {"marka": "Hyundai", "modelis": "i30", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.4, 2.0], "gadi": list(range(2007, 2024))},
        {"marka": "Hyundai", "modelis": "i40", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2011, 2021))},
        {"marka": "Hyundai", "modelis": "ix20", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.4, 1.6], "gadi": list(range(2010, 2021))},
        {"marka": "Hyundai", "modelis": "Kona", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.0, 1.6], "gadi": list(range(2017, 2024))},
        {"marka": "Hyundai", "modelis": "Santa Fe", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 3.5], "gadi": list(range(2000, 2024))},
        {"marka": "Hyundai", "modelis": "Sonata", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 3.3], "gadi": list(range(1985, 2024))},
        {"marka": "Hyundai", "modelis": "Tucson", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 2.4], "gadi": list(range(2004, 2024))},
        {"marka": "Hyundai", "modelis": "Veloster", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.6], "gadi": list(range(2011, 2023))},
        {"marka": "Hyundai", "modelis": "Xcent", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.2, 1.4], "gadi": list(range(2014, 2024))},
        {"marka": "Nissan", "modelis": "Almera", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.2, 1.8], "gadi": list(range(2000, 2023))},
        {"marka": "Nissan", "modelis": "Micra", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.2], "gadi": list(range(1992, 2024))},
        {"marka": "Nissan", "modelis": "Note", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.2, 1.5], "gadi": list(range(2012, 2024))},
        {"marka": "Nissan", "modelis": "Qashqai", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.5, 2.0], "gadi": list(range(2007, 2024))},
        {"marka": "Nissan", "modelis": "Juke", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.5, 1.6], "gadi": list(range(2010, 2024))},
        {"marka": "Nissan", "modelis": "X-Trail", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 2.5], "gadi": list(range(2000, 2024))},
        {"marka": "Nissan", "modelis": "Pathfinder", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.5, 5.6], "gadi": list(range(2004, 2024))},
        {"marka": "Nissan", "modelis": "Navara", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.5, 3.0], "gadi": list(range(2005, 2024))},
        {"marka": "Nissan", "modelis": "GT-R", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [3.8], "gadi": list(range(2007, 2024))},
        {"marka": "Volvo", "modelis": "C30", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2006, 2014))},
        {"marka": "Volvo", "modelis": "S40", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2004, 2013))},
        {"marka": "Volvo", "modelis": "V50", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2004, 2013))},
        {"marka": "Volvo", "modelis": "S60", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 3.0], "gadi": list(range(2000, 2011))},
        {"marka": "Volvo", "modelis": "V70", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 3.0], "gadi": list(range(2000, 2011))},
        {"marka": "Volvo", "modelis": "S80", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 4.4], "gadi": list(range(1998, 2017))},
        {"marka": "Volvo", "modelis": "XC70", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.4, 3.2], "gadi": list(range(2000, 2017))},
        {"marka": "Volvo", "modelis": "S40 II", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2012, 2018))},
        {"marka": "Volvo", "modelis": "V40", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2012, 2020))},
        {"marka": "Volvo", "modelis": "S60 II", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2010, 2023))},
        {"marka": "Volvo", "modelis": "V60", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2010, 2023))},
        {"marka": "Volvo", "modelis": "S80 II", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 4.4], "gadi": list(range(2010, 2017))},
        {"marka": "Volvo", "modelis": "XC60", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 3.0], "gadi": list(range(2008, 2023))},
        {"marka": "Volvo", "modelis": "S90", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 3.0], "gadi": list(range(2016, 2023))},
        {"marka": "Volvo", "modelis": "V90", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 3.0], "gadi": list(range(2016, 2023))},
        {"marka": "Volvo", "modelis": "XC90", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.5, 3.2], "gadi": list(range(2002, 2023))},
        {"marka": "Volvo", "modelis": "XC40", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis", "Elektro"], "tilpums": [1.5, 2.0], "gadi": list(range(2017, 2023))},
        {"marka": "KIA", "modelis": "Rio", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.1, 1.6], "gadi": list(range(2000, 2024))},
        {"marka": "KIA", "modelis": "Picanto", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.0, 1.2], "gadi": list(range(2004, 2024))},
        {"marka": "KIA", "modelis": "Cerato", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.4, 2.0], "gadi": list(range(2004, 2024))},
        {"marka": "KIA", "modelis": "Ceed", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.4, 2.0], "gadi": list(range(2006, 2024))},
        {"marka": "KIA", "modelis": "Soul", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.0], "gadi": list(range(2009, 2024))},
        {"marka": "KIA", "modelis": "Sportage", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.6, 2.4], "gadi": list(range(2004, 2024))},
        {"marka": "KIA", "modelis": "Sorento", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.4, 3.8], "gadi": list(range(2002, 2024))},
        {"marka": "KIA", "modelis": "Stinger", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 3.3], "gadi": list(range(2017, 2024))},
        {"marka": "KIA", "modelis": "XCeed", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.4, 2.0], "gadi": list(range(2019, 2024))},
        {"marka": "Subaru", "modelis": "Impreza", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.5, 2.0], "gadi": list(range(1992, 2024))},
        {"marka": "Subaru", "modelis": "Legacy", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 3.6], "gadi": list(range(1989, 2024))},
        {"marka": "Subaru", "modelis": "Outback", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 3.6], "gadi": list(range(1995, 2024))},
        {"marka": "Subaru", "modelis": "Forester", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 2.5], "gadi": list(range(1997, 2024))},
        {"marka": "Subaru", "modelis": "XV", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.6, 2.0], "gadi": list(range(2012, 2024))},
        {"marka": "Subaru", "modelis": "BRZ", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [2.0], "gadi": list(range(2012, 2024))},
        {"marka": "Subaru", "modelis": "WRX", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [2.0, 2.5], "gadi": list(range(2002, 2024))},
        {"marka": "Subaru", "modelis": "WRX STI", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [2.5], "gadi": list(range(2004, 2024))},
        {"marka": "Subaru", "modelis": "Ascent", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.5], "gadi": list(range(2018, 2024))},
        {"marka": "Mazda", "modelis": "2", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [1.5, 2.0], "gadi": list(range(1999, 2024))},
        {"marka": "Mazda", "modelis": "3", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.5, 2.5], "gadi": list(range(1993, 2024))},
        {"marka": "Mazda", "modelis": "6", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.5, 3.0], "gadi": list(range(1970, 2024))},
        {"marka": "Mazda", "modelis": "CX-3", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.5, 2.0], "gadi": list(range(2015, 2024))},
        {"marka": "Mazda", "modelis": "CX-5", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [2.0, 2.5], "gadi": list(range(2012, 2024))},
        {"marka": "Mazda", "modelis": "CX-30", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns", "Dīzelis"], "tilpums": [1.5, 2.5], "gadi": list(range(2019, 2024))},
        {"marka": "Mazda", "modelis": "CX-9", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.5, 2.5], "gadi": list(range(2007, 2024))},
        {"marka": "Mazda", "modelis": "MX-5", "ak": ["Manuālā"], "degviela": ["Benzīns"], "tilpums": [1.5, 2.0], "gadi": list(range(1989, 2024))},
        {"marka": "Lexus", "modelis": "IS", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 3.5], "gadi": list(range(1999, 2024))},
        {"marka": "Lexus", "modelis": "GS", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 5.0], "gadi": list(range(1993, 2021))},
        {"marka": "Lexus", "modelis": "ES", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 2.5], "gadi": list(range(1989, 2024))},
        {"marka": "Lexus", "modelis": "LS", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [3.5, 5.0], "gadi": list(range(1989, 2024))},
        {"marka": "Lexus", "modelis": "RX", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 3.5], "gadi": list(range(1998, 2024))},
        {"marka": "Lexus", "modelis": "GX", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [4.6], "gadi": list(range(2002, 2024))},
        {"marka": "Lexus", "modelis": "LX", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [5.7], "gadi": list(range(1995, 2024))},
        {"marka": "Lexus", "modelis": "UX", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns",], "tilpums": [2.0], "gadi": list(range(2018, 2024))},
        {"marka": "Lexus", "modelis": "NX", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 2.5], "gadi": list(range(2014, 2024))},
        {"marka": "Lexus", "modelis": "RC", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [2.0, 5.0], "gadi": list(range(2014, 2024))},
        {"marka": "Lexus", "modelis": "LC", "ak": ["Manuālā", "automātiskā"], "degviela": ["Benzīns"], "tilpums": [5.0], "gadi": list(range(2017, 2024))}
    ]

    atbilstosie_auto = []
    for auto in automobili:
        if auto["marka"].upper() == marka.upper() and gads in auto["gadi"] and ak.upper() in [x.upper() for x in auto["ak"]] and degviela.capitalize() in [x.capitalize() for x in auto["degviela"]] and tilpums in auto["tilpums"]:
            atbilstosie_auto.append(auto['modelis'])

    return atbilstosie_auto

while True:
    print("<----------------------------------------------------------------->")

    def input_uppercase(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isalpha():
                return user_input.upper()
            else:
                print("Ievadījumam jābūt vārdam, lūdzu, ievadiet pareizu vērtību.")


    def input_number(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Ievadījumam jābūt skaitlim, lūdzu, ievadiet pareizu vērtību.")


    def input_float(prompt):
        while True:
            user_input = input(prompt)
            try:
                return float(user_input)
            except ValueError:
                print("Ievadījumam jābūt skaitlim, lūdzu, ievadiet pareizu vērtību.")


    marka = input_uppercase("Ievadiet auto marku: ")
    while marka not in automarkas:
        print("Šāda marka nav pieejama, lūdzu, izvēlieties no saraksta - Audi, BMW , Mercedes-Benz , Volkswagen , Toyota , Honda , Ford , Chevrolet , Hyundai , Nissan , Volvo , KIA , Subaru , Mazda , Lexus.")
        marka = input_uppercase("Ievadiet auto marku no saraksta: ")

    gads = input_number("Ievadiet auto gadu: ")
    ak = input_uppercase("Ievadiet auto ātrumkārbas tipu (Manuālā/Automātiskā): ")
    degviela = input_uppercase("Ievadiet auto degvielas tipu (Benzīns/Dīzelis): ").capitalize()
    tilpums = input_float("Ievadiet auto tilpumu: ")


    izvele = atrast_auto(marka, gads, ak, degviela, tilpums)
    if izvele:
        print(f"Atbilstošie automašīnas modeļi: {', '.join(izvele)}")
    else:
        print("Nekas netika atrasts, kas atbilstu jūsu kritērijiem.")
