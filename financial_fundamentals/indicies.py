'''
Created on Apr 6, 2013

@author: akittredge
'''



DOW_TICKERS = ['MMM', 'AA', 'AXP', 'T', 'BAC', 'BA', 'CAT', 'CVX', 
               'CSCO', 'DD', 'XOM', 'GE', 'HPQ', 'HD', 'INTC', 'IBM', 
               'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'PFE', 'PG', 'KO',
               'TRV', 'UTX', 'UNH', 'VZ', 'WMT', 'DIS']


# From wikipedia on 2013-4-1
S_P_500_TICKERS = ['A', 'AA', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACE', 'ACN', 
                   'ACT', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'ADT', 'AEE',
                    'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ',
                     'AKAM', 'ALL', 'ALTR', 'ALXN', 'AMAT', 'AMD', 'AMGN', 
                     'AMP', 'AMT', 'AMZN', 'AN', 'ANF', 'AON', 'APA', 'APC',
                      'APD', 'APH', 'APOL', 'ARG', 'ATI', 'AVB', 'AVP', 'AVY',
                       'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBBY', 'BBT', 'BBY',
                        'BCR', 'BDX', 'BEAM', 'BEN', 'BF.B', 'BHI', 'BIIB', 
                        'BK', 'BLK', 'BLL', 'BMC', 'BMS', 'BMY', 'BRCM', 
                        'BRK.B', 'BSX', 'BTU', 'BWA', 'BXP', 'C', 'CA', 
                        'CAG', 'CAH', 'CAM', 'CAT', 'CB', 'CBG', 'CBS', 'CCE',
                        'CCI', 'CCL', 'CELG', 'CERN', 'CF', 'CFN', 'CHK', 
                        'CHRW', 'CI', 'CINF', 'CL', 'CLF', 'CLX', 'CMA', 
                        'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNP', 'CNX',
                         'COF', 'COG', 'COH', 'COL', 'COP', 'COST', 'COV', 
                         'CPB', 'CRM', 'CSC', 'CSCO', 'CSX', 'CTAS', 'CTL',
                         'CTSH', 'CTXS', 'CVC', 'CVH', 'CVS', 'CVX', 'D', 'DD',
                         'DE', 'DELL', 'DF', 'DFS', 'DG', 'DGX', 'DHI', 'DHR',
                          'DIS', 'DISCA', 'DLPH', 'DLTR', 'DNB', 'DNR', 'DO',
                        'DOV', 'DOW', 'DPS', 'DRI', 'DTE', 'DTV', 'DUK', 'DVA',
                        'DVN', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL',
                        'EMC', 'EMN', 'EMR', 'EOG', 'EQR', 'EQT', 'ESRX', 
                        'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXPD',
                        'EXPE', 'F', 'FAST', 'FCX', 'FDO', 'FDX', 'FE', 
                        'FFIV', 'FHN', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLR',
                        'FLS', 'FMC', 'FOSL', 'FRX', 'FSLR', 'FTI', 'FTR',
                        'GAS', 'GCI', 'GD', 'GE', 'GILD', 'GIS', 'GLW',
                        'GME', 'GNW', 'GOOG', 'GPC', 'GPS', 'GRMN', 'GS', 'GT',
                        'GWW', 'HAL', 'HAR', 'HAS', 'HBAN', 'HCBK', 'HCN', 
                        'HCP', 'HD', 'HES', 'HIG', 'HNZ', 'HOG', 'HON', 'HOT', 
                        'HP', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSP', 'HST', 'HSY', 
                        'HUM', 'IBM', 'ICE', 'IFF', 'IGT', 'INTC', 'INTU', 'IP', 
                        'IPG', 'IR', 'IRM', 'ISRG', 'ITW', 'IVZ', 'JBL', 'JCI', 
                        'JCP', 'JDSU', 'JEC', 'JNJ', 'JNPR', 'JOY', 'JPM', 'JWN', 
                        'K', 'KEY', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 
                        'KR', 'KRFT', 'KSS', 'L', 'LEG', 'LEN', 'LH', 'LIFE', 
                        'LLL', 'LLTC', 'LLY', 'LM', 'LMT', 'LNC', 'LO', 'LOW', 
                        'LRCX', 'LSI', 'LTD', 'LUK', 'LUV', 'LYB', 'M', 'MA', 
                        'MAR', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 
                        'MDLZ', 'MDT', 'MET', 'MHP', 'MJN', 'MKC', 'MMC', 'MMM', 
                        'MNST', 'MO', 'MOLX', 'MON', 'MOS', 'MPC', 'MRK', 'MRO', 
                        'MS', 'MSFT', 'MSI', 'MTB', 'MU', 'MUR', 'MWV', 'MYL', 
                        'NBL', 'NBR', 'NDAQ', 'NE', 'NEE', 'NEM', 'NFLX', 'NFX', 
                        'NI', 'NKE', 'NOC', 'NOV', 'NRG', 'NSC', 'NTAP', 'NTRS', 
                        'NU', 'NUE', 'NVDA', 'NWL', 'NWSA', 'NYX', 'OI', 'OKE', 
                        'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PBI', 
                        'PCAR', 'PCG', 'PCL', 'PCLN', 'PCP', 'PCS', 'PDCO', 
                        'PEG', 'PEP', 'PETM', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 
                        'PHM', 'PKI', 'PLD', 'PLL', 'PM', 'PNC', 'PNR', 'PNW', 
                        'POM', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 
                        'PWR', 'PX', 'PXD', 'QCOM', 'QEP', 'R', 'RAI', 'RDC', 
                        'RF', 'RHI', 'RHT', 'RL', 'ROK', 'ROP', 'ROST', 'RRC', 
                        'RSG', 'RTN', 'S', 'SAI', 'SBUX', 'SCG', 'SCHW', 'SE', 
                        'SEE', 'SHW', 'SIAL', 'SJM', 'SLB', 'SLM', 'SNA', 'SNDK', 
                        'SNI', 'SO', 'SPG', 'SPLS', 'SRCL', 'SRE', 'STI', 'STJ', 
                        'STT', 'STX', 'STZ', 'SWK', 'SWN', 'SWY', 'SYK', 'SYMC', 
                        'SYY', 'T', 'TAP', 'TDC', 'TE', 'TEG', 'TEL', 'TER', 'TGT', 
                        'THC', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 
                        'TSN', 'TSO', 'TSS', 'TWC', 'TWX', 'TXN', 'TXT', 'TYC', 
                        'UNH', 'UNM', 'UNP', 'UPS', 'URBN', 'USB', 'UTX', 'V', 
                        'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSN', 'VTR', 
                        'VZ', 'WAG', 'WAT', 'WDC', 'WEC', 'WFC', 'WFM', 'WHR', 'WIN', 
                        'WLP', 'WM', 'WMB', 'WMT', 'WPO', 'WPX', 'WU', 'WY', 'WYN', 
                        'WYNN', 'X', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 
                        'YHOO', 'YUM', 'ZION', 'ZMH']


CLEANED_S_P_500_TICKERS = [ticker for ticker in S_P_500_TICKERS if '.' not in ticker] # yahoo doesn't like ADRs
CLEANED_S_P_500_TICKERS.remove('PPL') # edgar doesn't know about PPL
CLEANED_S_P_500_TICKERS.remove('ABBV') # no filings as of 2013-4-6
CLEANED_S_P_500_TICKERS.remove('ZION') # Edgar doesn't know about these guys
CLEANED_S_P_500_TICKERS.remove('MHP') # Or these people.