"""Configuration dictionary"""

hls_config = {
    "HLSS30.v2.0": {
        "assets": {
            "*": {
                "data_type": "int16",
                "nodata": -9999,
            },
            "Fmask": {
                "data_type": "uint8",
                "nodata": 255,
            },
        },
        "aliases": {
            "costal_aerosol": "B01",
            "blue": "B02",
            "green": "B03",
            "red": "B04",
            "red_edge_1": "B05",
            "red_edge_2": "B06",
            "red_edge_3": "B07",
            "nir_broad": "B08",
            "nir": "B8A",
            "water_vapour": "B09",
            "swir_1": "B11",
            "swir_2": "B12",
            "fmask": "Fmask",
        },
    },
    "HLSL30.v2.0": {
        "assets": {
            "*": {
                "data_type": "int16",
                "nodata": -9999,
            },
            "Fmask": {
                "data_type": "uint8",
                "nodata": 255,
            },
        },
        "aliases": {
            "costal_aerosol": "B01",
            "blue": "B02",
            "green": "B03",
            "red": "B04",
            "nir": "B05",
            "swir_1": "B06",
            "swir_2": "B07",
            "fmask": "Fmask",
        },
    },
}
