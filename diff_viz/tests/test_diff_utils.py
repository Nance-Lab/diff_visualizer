from diff_viz.diff_utils import get_experiment, get_csvs, get_geo_dict, get_geo_df, get_df_dose_list

file_path = 'diff_viz/tests/testing_data/msd_data/'

def test_get_experiment():
    date = '2019_01_01'
    donor = 'P17F'
    DIV = '3DIV'
    stimulus = 'OGD'
    level = '0.5h'
    experiment = get_experiment(date, donor, DIV, stimulus, level)
    assert experiment == '2019_01_01_P17F_3DIV_OGD_0.5h'

def test_get_csvs(file_path=file_path):
    
    geo_list = get_csvs(file_path, filetype='geomean')
    assert len(geo_list) == 2
    assert geo_list[0] == 'geomean_P17_1h_OGD_1d_40nm_slice_1_cortex_vid_1.csv'
    assert geo_list[1] == 'geomean_P17_NT_1d_40nm_slice_1_cortex_vid_1.csv'

def test_get_geo_dict(file_path=file_path):

    geo_list = get_csvs(file_path, filetype='geomean')
    doses = ['1h', 'NT']
    geo_dict = get_geo_dict(geo_list, doses)
    assert len(geo_dict) == 2
    assert '1h' in geo_dict.keys()
    assert 'NT' in geo_dict.keys()

def test_get_geo_df_geomean(file_path=file_path):

    #test geomean
    geo_df = get_geo_df(file_path, filetype='geomean', doses=['1h', 'NT'], timepoints=['1d'])
    assert geo_df.shape == (650, 2)
    assert geo_df.columns[0] == '1h_1d'
    assert geo_df.columns[1] == 'NT_1d'


def test_get_geo_df_geoSEM(file_path=file_path):
    #test geosem
    geo_df = get_geo_df(file_path, filetype='geoSEM', doses=['1h', 'NT'], timepoints=['1d'])
    assert geo_df.shape == (650, 2)
    assert geo_df.columns[0] == '1h_1d'
    assert geo_df.columns[1] == 'NT_1d'


def test_get_df_dose_list(file_path = file_path):

    # test geomean
    df_dose_list_geomean = get_df_dose_list(['1h', 'NT'], get_geo_df(file_path, filetype='geomean', doses=['1h', 'NT'], timepoints=['1d']))
    assert df_dose_list_geomean[0].shape == (650, 1)
    assert df_dose_list_geomean[1].shape == (650, 1)
    assert df_dose_list_geomean[0].columns[0] == '1h_1d'
    assert df_dose_list_geomean[1].columns[0] == 'NT_1d'

    # test geosem
    df_dose_list_geosem = get_df_dose_list(['1h', 'NT'], get_geo_df(file_path, filetype='geoSEM', doses=['1h', 'NT'], timepoints=['1d']))
    assert df_dose_list_geosem[0].shape == (650, 1)
    assert df_dose_list_geosem[1].shape == (650, 1)
    assert df_dose_list_geosem[0].columns[0] == '1h_1d'
    assert df_dose_list_geosem[1].columns[0] == 'NT_1d'