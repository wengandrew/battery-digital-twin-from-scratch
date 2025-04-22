"""
Plotting utilities
"""


def initialize(plt):
    """
    Initialize the plot configuration
    """

    plt.rc('font', **{'family' : 'serif',
                  'serif' : ['Times New Roman'],
                  'size': 16
                  })

    plt.rc('figure', **{'autolayout' : False,
                    'figsize'    : (6, 6)
                    })

    plt.rc('xtick', labelsize='medium')
    plt.rc('ytick', labelsize='medium')
    plt.rc('axes',  labelsize='medium', grid=True)
    plt.rc('axes',  titlesize='medium')
    plt.rc('legend', fontsize='medium')
    plt.rc('image',  cmap='gray')

    plt.rc('text.latex', preamble=r'\usepackage{times}')
