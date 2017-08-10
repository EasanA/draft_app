from draft.database import session, Player, Scoring  
import xlrd

class SeedParam(object):
    sheetname = ""
    namelow = 0
    namehigh = 0
    batterlow = 0
    batterhigh = 0
    pitcherlow = 0
    pitcherhigh = 0

def seed(seedparam):
    book = xlrd.open_workbook(seedparam.sheetname)
    sheet0 = book.sheet_by_name("Filtered-H")
    player_position = {}
    for j in range(seedparam.namelow,seedparam.namehigh):
        name = sheet0.cell(j,0).value
        position = sheet0.cell(j,18).value
        player_position[name] = position
    sheet1 = book.sheet_by_name("Projection-H")
    
    for j in range(seedparam.batterlow, seedparam.batterhigh):
        if sheet1.cell(j, 2).ctype == xlrd.XL_CELL_ERROR:
            batter = Player(
                name = sheet1.cell(j,0).value,
                position = player_position[name]
                )
        else:
            name = sheet1.cell(j,0).value
            position = player_position[name]
            batter= Player(
            name = name,
            position = position,
            batter_pa = sheet1.cell(j,2).value,
            batter_ab = sheet1.cell(j,3).value,
            batter_r = sheet1.cell(j,4).value,
            batter_hit = sheet1.cell(j,5).value,
            batter_single =sheet1.cell(j,6).value,
            batter_double = sheet1.cell(j,7).value,
            batter_triple = sheet1.cell(j,8).value,
            batter_hr = sheet1.cell(j,9).value,
            batter_bb = sheet1.cell(j,13).value,
            batter_sb = sheet1.cell(j,11).value,
            batter_cs = sheet1.cell(j,12).value,
            batter_k =sheet1.cell(j,14).value,
            batter_rbi = sheet1.cell(j,10).value,
            batter_avg = sheet1.cell(j,15).value,
            batter_obp = sheet1.cell(j,16).value,
            batter_slg = sheet1.cell(j,17).value,
            batter_ops = sheet1.cell(j,18).value,
            batter_errors_per_pa = sheet1.cell(j,189).value,
            batter_gidp_per_pa = sheet1.cell(j,190).value, 
            batter_hbp_per_pa = sheet1.cell(j,191).value,
            batter_xbh = sheet1.cell(j,7).value +  sheet1.cell(j,8).value +
            sheet1.cell(j,9).value,
        )
        session.add(batter)
        session.commit()
    
    sheet2 = book.sheet_by_name("Projection-P")
    print(seedparam.pitcherlow, seedparam.pitcherhigh)
    
    for j in range(seedparam.pitcherlow, seedparam.pitcherhigh):
        if sheet2.cell(j, 2).ctype == xlrd.XL_CELL_ERROR:
            pitcher = Player(
                name = sheet2.cell(j,0).value,
                position = player_position[name]
                )
        else:
            name = sheet2.cell(j,0).value
            position = player_position[name]
            pitcher = Player(
                name = name,
                position = position,
                pitcher_w = sheet2.cell(j,2).value,
                pitcher_l = sheet2.cell(j,3).value,
                pitcher_ip = sheet2.cell(j,4).value,
                pitcher_hit = sheet2.cell(j,5).value,
                pitcher_bb = sheet2.cell(j,6).value,
                pitcher_k = sheet2.cell(j,7).value,
                pitcher_er = sheet2.cell(j,8).value,
                pitcher_s = sheet2.cell(j,9).value,
                pitcher_era = sheet2.cell(j,10).value,
                pitcher_whip = sheet2.cell(j,11).value,
                pitcher_k9 = sheet2.cell(j,12).value,
                pitcher_qs =sheet2.cell(j,13).value,
                pitcher_gs = sheet2.cell(j,14).value,
                pitcher_g = sheet2.cell(j,15).value,
                pitcher_hra = sheet2.cell(j,16).value,
                pitcher_cg_per_gs = sheet2.cell(j,167).value,
                pitcher_shutout_per_gs = sheet2.cell(j,168).value,
                pitcher_hold = sheet2.cell(j,169).value,
                pitcher_bs = sheet2.cell(j,176).value,
        )
        session.add(pitcher)
        session.commit()

    score = Scoring(
            batter_single = 1,
            batter_double = 2,
            batter_triple = 3,
            batter_hr = 5,
            batter_bb = 1,
            batter_sb = 2,
            batter_cs = -1,
            batter_k = -1,
            batter_r = 1,
            batter_rbi = 1,
            batter_errors = -1,
            batter_gidp = -1,
            batter_hbp = 1,
            pitcher_w = 5,
            pitcher_l = -5,
            pitcher_ip = 1.5,
            pitcher_hit = -.5,
            pitcher_bb = -1,
            pitcher_k = 1,
            pitcher_er = -1,
            pitcher_s = 10,
            pitcher_qs = 10,
            pitcher_shutout = 10,
            pitcher_cg = 10,
            pitcher_bs = -5,
        )
    session.add(score)
    session.commit()