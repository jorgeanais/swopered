import astropy.io.fits as fits
from glob import glob
from pathlib import Path
from astropy.table import Table


def create_table_from_images(data_dir: Path) -> Table:
    """
    This function reads a directory where fits images are expected to be. 
    From these files it constructs a table using the header information about the images.
    """


    for fits_file in data_dir.glob("*.fits"):
        with fits.open(fits_file) as hdul:
            hdu = hdul[0]
            header = hdu.header

        data = {
            "filename": header["FILENAME"],
            "exptype": header["EXPTYPE"],
            "object": header["OBJECT"],
            "exptime": header["EXPTIME"],
            "filter": header["FILTER"],
            "ra": header["RA"],
            "ra_d": header["RA-D"],
            "dec": header["DEC"],
            "dec_d": header["DEC-D"],
            "equinox": header["EQUINOX"],
            "telfocus": header["TELFOCUS"],
            "airmass": header["AIRMASS"],
            "ut_date": header["UT-DATE"],
            "ut_time": header["UT-TIME"],
            "ut_end": header["UT-END"],
            "path": fits_file.resolve(),
        }

    return Table(data)
