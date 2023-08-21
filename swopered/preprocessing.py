from glob import glob
from pathlib import Path

import astropy.io.fits as fits
from astropy.table import Table


def create_table_from_fits(data_dir: Path) -> Table:
    """
    This function reads a directory where fits images are expected to be. 
    From these files it constructs a table using the header information about the images.
    """

    df_data = []

    for fits_file in sorted(data_dir.glob("*.fits")):
        with fits.open(fits_file) as hdul:
                hdu = hdul[0]
                header = hdu.header
        
        df_data.append({
                "file": header["FILENAME"][:-2],
                "quadrant": header["FILENAME"][-2:],
                "exptype": header["EXPTYPE"],
                "object": header["OBJECT"],
                "exptime": header["EXPTIME"],
                "filter": header["FILTER"],
                "ra": header["RA"],
                "dec": header["DEC"],
                "dec_d": header["DEC-D"],
                "ra_d": header["RA-D"],
                "equinox": header["EQUINOX"],
                "telfocus": header["TELFOCUS"],
                "airmass": header["AIRMASS"],
                "ut_date": header["UT-DATE"],
                "ut_time": header["UT-TIME"],
                "ut_end": header["UT-END"],
                "path": str(fits_file),
            })

    return Table(df_data)
