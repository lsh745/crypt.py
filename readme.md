# Readme

You can use this for decrypt Caesar or Vigenere cipher.


## Argv

> **C**iphertext : **-c**, For ciphertext.
>
> **K**ey : **-k**, Use this if you know the key of the Vigenere cipher.
>
> **G**uess : **-g**, Use with **-t** if you know **-g** is **-t**.
>
> **T**arget : **-t**, Must use with **-g**
>
> **P**lus/**M**inus : **-pm**, Default is '-'. If you want to change the Caesar or Vigenere ciphers calculation direction.



## Examples

### Caesar(only **-c**)

```
❯ python3 crypt.py -c "flag is HackCTF{v_jvyy_3rzrz0r3_lbh.qba'g_sbetrg_zr_gbb}"

❯  0 : flag is HackCTF{v_jvyy_3rzrz0r3_lbh.qba'g_sbetrg_zr_gbb}
 1 : gmbh jt IbdlDUG{w_kwzz_3sasa0s3_mci.rcb'h_tcfush_as_hcc}
 2 : hnci ku JcemEVH{x_lxaa_3tbtb0t3_ndj.sdc'i_udgvti_bt_idd}
 3 : iodj lv KdfnFWI{y_mybb_3ucuc0u3_oek.ted'j_vehwuj_cu_jee}
 4 : jpek mw LegoGXJ{z_nzcc_3vdvd0v3_pfl.ufe'k_wfixvk_dv_kff}
 5 : kqfl nx MfhpHYK{a_oadd_3wewe0w3_qgm.vgf'l_xgjywl_ew_lgg}
 6 : lrgm oy NgiqIZL{b_pbee_3xfxf0x3_rhn.whg'm_yhkzxm_fx_mhh}
 7 : mshn pz OhjrJAM{c_qcff_3ygyg0y3_sio.xih'n_zilayn_gy_nii}
 8 : ntio qa PiksKBN{d_rdgg_3zhzh0z3_tjp.yji'o_ajmbzo_hz_ojj}
 9 : oujp rb QjltLCO{e_sehh_3aiai0a3_ukq.zkj'p_bkncap_ia_pkk}
10 : pvkq sc RkmuMDP{f_tfii_3bjbj0b3_vlr.alk'q_clodbq_jb_qll}
11 : qwlr td SlnvNEQ{g_ugjj_3ckck0c3_wms.bml'r_dmpecr_kc_rmm}
12 : rxms ue TmowOFR{h_vhkk_3dldl0d3_xnt.cnm's_enqfds_ld_snn}
13 : synt vf UnpxPGS{i_will_3emem0e3_you.don't_forget_me_too}
14 : tzou wg VoqyQHT{j_xjmm_3fnfn0f3_zpv.epo'u_gpshfu_nf_upp}
15 : uapv xh WprzRIU{k_yknn_3gogo0g3_aqw.fqp'v_hqtigv_og_vqq}
16 : vbqw yi XqsaSJV{l_zloo_3hphp0h3_brx.grq'w_irujhw_ph_wrr}
17 : wcrx zj YrtbTKW{m_ampp_3iqiq0i3_csy.hsr'x_jsvkix_qi_xss}
18 : xdsy ak ZsucULX{n_bnqq_3jrjr0j3_dtz.its'y_ktwljy_rj_ytt}
19 : yetz bl AtvdVMY{o_corr_3ksks0k3_eua.jut'z_luxmkz_sk_zuu}
20 : zfua cm BuweWNZ{p_dpss_3ltlt0l3_fvb.kvu'a_mvynla_tl_avv}
21 : agvb dn CvxfXOA{q_eqtt_3mumu0m3_gwc.lwv'b_nwzomb_um_bww}
22 : bhwc eo DwygYPB{r_fruu_3nvnv0n3_hxd.mxw'c_oxapnc_vn_cxx}
23 : cixd fp ExzhZQC{s_gsvv_3owow0o3_iye.nyx'd_pybqod_wo_dyy}
24 : djye gq FyaiARD{t_htww_3pxpx0p3_jzf.ozy'e_qzcrpe_xp_ezz}
25 : ekzf hr GzbjBSE{u_iuxx_3qyqy0q3_kag.paz'f_radsqf_yq_faa}
```



### Vigenere that knows key(-c and -k)

```
❯ python3 crypt.py -c "Rijvsmysmysmy Itovwyrc! Ns wyy ixsu Glm kq G? wc lkqc sw qwsmdlkkr sr...M ixsu fipi acvp urer iss geld! Md iss mel niastfov rrmq mvwzxmqvyw, cme gyx kcd xfo gmbvcmx yxwuov. qy, jjkk gc LymoADJ{t_tzwi_3vxbd0p3_vff.afy'q_wzoxpq_dp_qfz}" "flag is HackCTF{v_jvyy_3rzrz0r3_lbh.qba'g_sbetrg_zr_gbb}" -k "Key"

❯ Hellooooooooo Everyone! Do you know Who am I? my name is smoothman uh...I know very well what you want! If you can decipher this cryptogram, you can get the correct answer. so, flag is HackCTF{v_jvyy_3rzrz0r3_lbh.qba'g_sbetrg_zr_gbb}
```



### Vigenere that have to match(-c, -g, 0t)

```
❯ python3 crypt.py -c "Rijvsmysmysmy Itovwyrc! Ns wyy ixsu Glm kq G? wc lkqc sw qwsmdlkkr sr...M ixsu fipi acvp urer iss geld! Md iss mel niastfov rrmq mvwzxmqvyw, cme gyx kcd xfo gmbvcmx yxwuov. qy, jjkk gc LymoADJ{t_tzwi_3vxbd0p3_vff.afy'q_wzoxpq_dp_qfz}" -g "LymoADJ" -t "HackCTF"

❯ KEY : KEY
Hellooooooooo Everyone! Do you know Who am I? my name is smoothman uh...I know very well what you want! If you can decipher this cryptogram, you can get the correct answer. so, flag is HackCTF{v_jvyy_3rzrz0r3_lbh.qba'g_sbetrg_zr_gbb}
```

