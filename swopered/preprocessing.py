import astropy.io.fits as fits
from glob import glob
from os import path
from astropy.table import Table


def ls(dir):
    """
    This function reads a directory where fits images are expected to be. From this files it constructs a table
    from the header of the images.

    :param dir: string with the path to the directory
    :return: Astropy Table
    """
    cols = ['file', 'exptype', 'object', 'exptime', 'filter', 'ra', 'ra_d', 'dec', 'dec_d', 'ut_date', 'ut_time',
            'airmass', 'observer', 'binning', 'opamp']
    file_list = glob(path.join(dir, '*c1.fits'))
    file_list.sort()
    rows = []

    for file in file_list:
        with fits.open(file) as hdul:
            hdu = hdul[0]
            header = hdu.header

        exptype = header['EXPTYPE']
        object = header['OBJECT']
        exptime = header['EXPTIME']
        filter = header['FILTER']
        ra = header['RA']
        ra_d = header['RA-D']
        dec = header['DEC']
        dec_d = header['DEC-D']
        ut_date = header['UT-DATE']
        ut_time = header['UT-TIME']
        airmass = header['AIRMASS']
        observer = header['OBSERVER']
        binning = header['BINNING']
        opamp = header['OPAMP']

        rows.append((file, exptype, object, exptime, filter, ra, ra_d, dec, dec_d, ut_date, ut_time,
                     airmass, observer, binning, opamp))

    return Table(names=cols, rows=rows)