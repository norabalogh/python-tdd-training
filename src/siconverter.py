def siconverter(val, unit_in, unit_out):
    SI = {'mikrom': 1e-6, 'mm': 0.001, 'cm': 0.01,
          'dm': 0.1, 'm': 1.0, 'km': 1000}
    output = val*SI[unit_in]/SI[unit_out]
    return output
