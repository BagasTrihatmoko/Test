import itertools
def compute():
	ans = sum(1
		for s in WORDS
		if is_triangular_number(sum((ord(c) - ord('A') + 1) for c in s)))
	return str(ans)


def is_triangular_number(n):
	temp = 0
	for i in itertools.count():
		temp += i
		if n == temp:
			return True
		elif n < temp:
			return False


WORDS = [  
	"A","PUVVAIO", "SEZHT", "SOXLAN", "TKBK", "AKBD", "RSHFJ", "BTSXZZI", "LXO", "RWNZLY", 
		"PLOMGJZ", "HDUVNW", "KQDH", "LYEKCN", "ASLSXYA", "SDUQNN", "JTULGXY", "FBRWI", "CCHDKLS",
		"RVMEP", "HADP", "CXPNZ", "KPDNEY", "ETNF", "RLFJFH", "OXCXFFG", "UGSEV", "EXZZ", "UVEPX", 
		"QGIT", "LMYHBP", "FTPQHKI","UDY", "LVDP", "BMQNV", "FWLEEBU", "SNPB","ZKSVN", "PXPAVEH", 
		"OGIA", "DEN", "YAXA", "MOQG", "YXEEL", "PBTIVN", "UVWAI", "DGHZKBV", "QUHFVRI", "OISHL",
		"KGH", "BRIOXGH", "ZGYXZX", "ZXCOGVU", "MBSG", "FKVHU", "YKFPGKP", "KRJPW", "KAJWLZZ", "ZKZ",
		"HRAKQBV", "YQBB", "SMM", "XSCTMQ", "TSBJ", "EPRKLFD", "CEF", "NXB", "FLRVYQ", "RNC", "DVDK",
		"KAL", "TDDAXV", "STQPRVV", "JJNV", "GYHJ", "XJQ", "ARF", "HAL", "SLO", "DTCCL", "UTXM", "NEXOXT",
		"LPIN", "DNGOF","JEBPBJE", "HJQAZ", "BCQH", "SVKHBL", "ENPMW", "ZYSXGMS", "ALMEU", "LDQWERK", 
		"WHHYY", "YHY", "QYQUAXW", "FMXN", "BWW", "GTVAPEX", "UXQXL", "PHGE", "NUYWDY", "WGNQK", "NUJIUGR",
		"QNWIH", "SGLMA","LVQZQ", "UCRI", "UJQPBWS", "UXYKJA", "VIHCCQW", "XZI", "BFKXD", "IVVGK", "DKZ",
		"NIRPJ", "YAP", "UIAIQ", "LTVFBAH", "EWGBQQO", "GOOAJR", "CVPTXNS", "ZHUBUQD", "JZPMUY", "OHEN",
		"RJXXJAT", "IITSZ", "CSTQIFO", "AHY","QUG", "IGQUDFX", "JVWIDGM", "EBBGHQF", "VITRZ", "TMFL", 
		"BEAW", "XEUZLJ", "VNDBLVD", "RQG", "MMC", "EOFAMW", "PSSAT", "VKFBF", "CWBG", "KMM", "UEA", 
		"LBYK", "YII", "SGJUF", "LXRVPU", "BPGHHJH", "OJKBSCE", "PYI", "VJI","CFCOCH", "QMZRZZ", "JQQJ",
		"HHU", "KOSIAP", "NJPOK", "NOCZ", "IJC", "SFXAL", "PJWL", "CZKLO", "ZNT", "KJIKPFN", "AQKUSDF",
		"SIKJPRB", "HVIZ", "PSVWG", "GNO", "ULHK", "ZZF", "IPEW", "DFJTLQ", "CYWSYJ", "DIAXUM", "DIYHU","UVG",
		"AXAVYEO", "LKXL", "ZBUWS", "TSAEYOF", "DRQKLMQ", "BDXEOIM", "VCCOAI", "NZS", "NOC", "HEXHYBV", 
		"DWVVRKK", "GNUE", "ZSUM", "SDFZCID", "AYP", "DTPZVMH", "FWPAG", "PIEE", "LQBK", "UUECHW", "WIL", 
		"AIQ", "BKDMEAM", "LDW", "OALWT", "ZPRCWA", "ZDZ", "BWUU", "FJLREAD", "XVHSHNJ", "QGVKRIJ", "JEJUB",
		"TACZOYQ","HXJXZY", "SFVA", "RVPHLOT", "MSREU", "OSL", "QKX", "KYKKOHQ", "OFY", "LFQU", "MGMU", "OMAR",
		"RWHH", "PMEXQN", "GFP", "NSMSJ", "QZGUAT", "QOPJUJS", "EZKCJK", "KGKRV", "PBN","BPAXEOI", "IOGTZC", 
		"WMQIK", "IQHL", "LFMCPPB", "JKHGM", "IBECWZ", "YJYZWV", "PQT", "YEG", "PZNCDPD", "DISH", "BLVUG", 
		"OYBSGK", "MDKGZW", "NSGSRO", "SOYXV", "FPWV", "GLUGW","EFBFBWL","YDHXBX", "TZJA", "CFFA", "SSLXT",
		"UNLM", "PVFHRC"," MGTP", "VYRPW", "OIMBNQC"," LIAY", "YKWVJ", "HPZMJ", "DUDHM", "DYNIOG", "JQQD", 
		"BNS", "RAXYH", "PPRS", "RSR", "GMJT", "EFW","CY", "IQDXAD", "YVZ", "LLWDP", "JRKVUK", "QHQ", "EQZXE",
		"ZHYDHM", "FXP", "NLRMB", "AVWFES", "KPDJSU", "NTGSJFD", "KSKKTJ", "QPAXJ", "LQUWA", "TYBFDYK", "IRDTIVA",
		"XKHDE", "XKCS", "YUVUG", "OYLAK", "JGO", "EAN", "AFW", "GKIOCGO", "SPSUQ", "VIQAVFE", "IKM", "SUHUYBA", 
		"LAPWKTJ", "ITHMGU", "EDF", "GAQ", "HHWDOOA", "YTCNKP", "XEDYZXX", "WPKG", "FZNMPP", "EFENSY", "JOC", 
		"FCNPQH", "YSXXC", " WRJFUC", "LKYDQ", "FHMCHY", "TWBQ", "HBYBLK", "YHEVVNT", "FEKKTD", "MUIB",
		"KUOAENN", "JECRJ", "GHHE", "NJYP", "XKX", "MESEAT", "GZMALAK", "FUUUH", "YRR", "AAKFM", "VMDI",
		"FCHNMK", "VAZ","AEYWNTA", "VTU", "EEOE", "YQHRQYW", "RYZI", "WRPWP", "KBNXQ", "YZCTK", "VPQL", "KUSYLM",
		"XWOCUUC", "RRIYEL", "OXGVPP", "XZBBYZ", "MXK", "XHTWYI", "JURIRNH","TTEGSD", "JPTMHXE", "BNJXHLO", "LIY",
		"BHVI", "PLALR", "GRDJGMG", "MJWEODC", "WPPWEG", "YZIHO", "XMFX", "IJJ", "YVRHO", "EFQDZWD", "WZSVACN",
		"XKJKM", "GJQPTX", "QWFK", "MHNDYBJ", "DMBYGP", "MUGT", "YNPS", "TBAOI", "FEMDLIJ", "VREKYD", "PDRUG",
		"ISMENHM", "UNVMJZT", "LHPKQS", "UOKLBVD", "NLESQ", "PVAV", "YWWBKJZ", "TEEI", "TRYBZY", "MGTGK", "DMXV",
		"CJOBWH", "HWTBBEO", "QZMGGIM", "TTDEWP", "IHXC", "MYELQB", "MQYIS", "ULSB", "WNBAIZ", "OPICS", "NTQTXS",
		"NJXPQ", "AXHV", "CGE", "QKXLQ", "PHWDBP", "URK", "ZZZTUX","GMBFIDN", "JIW", "GXOB", "DDK", "XPWZWMZ", 
		"DVOJZKP", "MHTCRX", "HMAR", "YBOFCZT", "WEOZSYS", "AIUGQQY" ,"QVCE", "JSAMG", "JECUJK", "NLEMDL", "ZHCP",
		"RMGGE", "QUNQ", "BKL", "UMOMPX", "WUCP", "HHQM", "NJFQ", "ATZ", "KCNYVZJ", "BXDX", "HUQF", "WSBD", "MORVX",
		"GXFR", "XRZLSP", "WISX", "GJXEPI", "FDUDGPM", "PUHPYX", "NDWSMOJ", "AWOXXK", "KJF", "AIMTMP","QFMBQJM", 
		"GFXFXW", "PRJ", "BNJ", "CXODJF", "KLTXM", "KZC", "FEKK", "NJP", "MCBZ", "KVTGOIJ", "MZLAPND", "GDKLAIQ",
		"XOP", "FXRU", "MRIZFWH", "TIJQATO", "OXDAVWU", "UKSVZIF", "IEMR", "NGCELD", "YXCHOGK", "BNHQ", "OGPPN", 
		"QIKJRT", "CWMZT", "HBLH", "XNEY", "YTUAP", "SJODVM", "ZVP", "HVB", "LUOQMVU", "HOX", "WFKSOP", "XZNN", 
		"SQET", "NVJE", "JQGGI", "LXDCY", "NNGYZ", "UPDL", "SVXVKUE", "MNPV", "MXKWWRP", "JZXEET", "GMPFV", "TSXJSOI",
		"CDJDG", "LMYK", "OLUXYW", "KYVBB", "XNUT", "WWUXMPV", "GGGA", "ULGYW", "AKOQRA", "WHINAK","FJTO", "QMJFSY", 
		"NBPWV", "MQCVKKX", "SLT", "GSPML", "QFHCOBB", "SAOQXKZ", "PTMAVWZ", "FAFYHEJ", "KJPMC", "UQM", "NFGXCH", 
		"OBLXOJ", "LJA", "QLYI", "LZCQ", "OYV", "QVQPDQC","CEVEXU", "UPGQP", "RINZV", "LUCPUU", "QYVCIJH", "WQKE", 
		"PKFMDS", "OJDI", "VPGPFSG", "DDQUERQ", "RKNKS", "ZPQ", "KNWWE", "GIJ", "PEW", "TZKZL", "EAL", "PHNTQ", 
		"AWQZRT", "KYNHHCS", "DNTCTEL", "IFA", "VWUUIDY", "JCDANUC", "IEJK", "MURIVEX", "DPUUN", "BJKXSQ", "YQQW",
		"BINVBOJ", "FXWLQYO", "CBPNM", "THV", "TLRF", "WVV", "WWE", "NHDY", "SWLP","NOAT", "YVGS", "YFRPZ", "NFR", 
		"VGDG", "CPIR", "KYMDRBT", "EOV", "XMYQLD", "GAPUWJA", "HNBFH", "PCVJT", "MAJXEZ", "QJOS", "MBDSEC", "TDNWIJO",
		"DJA", "BDOCLAA", "CRKTCVV", "DMFB", "AGXW", "AXAPL", "JOA", "VJFZC", "VWE", "WNMHA", "XGLEO", "IXZLUXG", "QAOFTAI",
		"JFHS", "RWFQDQS", "UPVWNUM", "ZEDPUK", "OSOKY", "SLDNMP", "SXNEFD", "ZZG", "JWFF", "MEJHYV", "LGKWKHE", "VTIZWBE", 
		"JPMNHX", "DOAHI", "QUURMJ", "VFFOWG", "EWMPDL", "AQMICEZ", "FOYSST", "RTXTE", "KKFC", "JYQ", "KZGOAT", "JQCHI", 
		"GFTJUU", "SYATBT", "REVLG", "TKD", "VQVTMX", "ECPUY", "JWUHBZM", "ERM", "WZKMLZ", "CTWN", "STSLICZ", "NVINIO", 
		"YBAVVQ", "VCFOYDM", "CHGD", "WUGO", "LUOKXE", "SPIBE", "VGZFLT", "OTQ", "UOSO", "WQX", "NXDEV","WJP", "XAQZJDC",
		"KUTTQJ", "RWWHOQ", "MFPQWU", "RIKE", "LCRZKSG", "VBIE", "GTT", "ZXNKHX", "LCZRS", "LPPB", "HDHGM", "DOZRI", "AQH", 
		"CZXD", "YGIJFL", "QKJC", "WMPOFN", "EMFXFZ","DIUTPQ", "IJE", "AXDJ", "PNXXWR", "GRRF", "IJIJAOM", "TVTOWQP", "RXPOK", 
		"ZPU", "AGGJ", "NZOTUE", "HYDQU", "UHUCC", "MAVYF", "KCOM", "NECNO", "MNBT", "UTZIZZP", "QHPH", "USTQS","VSU", "EAXBAUM",
		"WPTSB", "DHB", "TAOX", "YQW", "IPLFF", "NAUDV", "WSIMFB", "SRSFP", "CYRPM", "KLETOI", "MVG", "HDUR", "XSNU", 
		"PIKGOCP", "URKFSS", "UBLCJTX", "HYTJE", "YWNFS","ETJSBF","CLEL", "BMHF", "TDKDOQJ", "AXDGXVX", "MGSZ", 
		"KNEQZWR", "OAXQB", "LRYZQ", "XEQ", "LAK", "ERY", "KVGYXIN", "FSYRA", "JMACWY", "JTDZKGV", "KOR", "ARK",
		"HNYTJZ", "OWJCQ","VDILN", "WCAGLD", "UVZ", "QWUL", "EHR", "ZOJQC", "XKNLEXS", "DYSFQ", "YKR", "EZDXY", 
		"KSYPA", "PLF", "CCZCZ", "PQMYFP", "RJG", "XTWCD", "TONPLWB", "TNYD", "CAT", "JFY", "QXFDOMH", "CCVHIRO",
		"WFDTM", "XWKU", "REOEEGM", "DZW", "KJOXM", "EAGBBS", "SHFF", "DTAVH", "MMQR", "VBWWHXD", "DKWQQQG", "ZMIZLQI",
		"UGM", "UKABBS", "HRF", "HCO", "BDNEW", "XQSR", "DWJGQI","ULPPDM", "GHX", "FPTQ", "LZTH", "CECAIQ", "IFIMCOR",
		"SVPF", "COEGZAA", "WYJKL", "YZOQIVG", "MTCP", "IPU", "OVZOO", "QALWW", "HDTS", "QYDDMDJ", "ABPJDPE", "LKUKF", 
		"CWY", "JRBHVK", "VHBJZJH", "RKPHLMG", "DHJ", "FCNX", "OIXE", "XAW", "IVNPM", "RPPELBX", "HXAXGD", "SZMCPMS", 
		"KDWI", "ETRJUKH", "XVEP", "PBSUPXC", "YEVUHU", "LSCR", "HBXSDWZ", "FLGNKD", "ZDAF", "VQH", "QDNEQ", "UUKZF", 
		"TQSTV", "TCQQP", "FIUO", "YQLSJEG", "CSGPML", "JMF", "CGHB", "WIF", "NLXF", "BHI", "WDAHPT", "YGOGM", "EGJP",
		"IKEV", "DCMN", "VARIDJ", "VIFNZVN", "PGTVTL", "SRM", "XCY", "EEOZ", "FVG", "XRTM", "OCTUQ", "ZDHW", "YDLT", 
		"GHTEA", "RHHT", "QXGUGJ", "NKU", "KOG", "JKSBEQA", "URYB", "QARJVPU", "MYP", "PCLF", "KCGMY","XKCYVT", "RZGOC",
		"ALO", "URVHHE", "KXIECO", "KHQ", "OQRD", "PSOARP", "XFHHAQ", "RYEB", "OUVKE", "BIDOW", "IVME", "QPRQ", "AHJJ", 
		"VJZ", "ZTIKKV", "GCR", "QCTTA", "CHBKRO", "BFSKSL", "SRA", "RAKEY", "YAMX", "CTAQF", "TYAIY", "XBOQTQP", "XBYIG", 
		"UFXOO", "AJQMOM", "EXYQS", "OGJKTIV", "SKJ", "VQNN", "VTKO", "JDB", "QQJYF", "GFBSHYZ", "UOM", "IGU", "FAL", "TYF", 
		"TDIW", "RKRW", "PVYIV", "UQDXES", "ONMTUG", "OAVTCG", "TAP", "UYCNQ", "ECUOCX", "KLEO", "RPZKEP", "RTW", "ZNHTAF", 
		"YUPAURB", "GRS", "XXVDLZ", "VBUDA", "BGK","YJJ", "ZWTHV", "PUHTDX", "KXWAL", "KCOVF", "VZTHXYN", "CZDG", "QYRKGG", "LSV",
		"PET", "SIYHHE", "WAHBXT", "DIHJ", "QHXBSS", "SJCKY", "VOLR", "HELW", "PAQZU", "SUXP", "XYA", "SGOYDNZ", "YAWM", "IEP",
		"YQLQN", "PQUZK", "PLUTZZ", "ZHX", "YMZTY", "QJDPY", "ZZEJV", "RUV", "LJKF", "GIT", "JXASYPZ", "NQECKV", "CNTMCA", "DWJ",
		"AYMQW", "YJWW", "GNQFU", "PRX","ITJU", "LTW", "LQRQ", "WAGWIRB", "IGOAQQU", "WDGXXC", "VRSYU", "IXPGMF", "YUSRCD", "HVESB",
		"SNJLSTJ", "TPN", "QVI", "MZSO", "GNH", "DBHPF", "VWTPI", "LXHD", "VHDLUIQ", "VRTTQI", "TUHAC", "YBD", "XRU", "LCYXF",
		"VBJE", "JNMKENB", "CQXUC", "VKKP", "XYGM", "OEQYUKA", "YOUTOTY", "WBCEUAD", "HHZ", "BYMK", "UVLLGO", "WQCWZE",
		"MIBNKMX", "QSQZYVS", "DJRMC", "WYJAVYT", "KQMTW", "ONGYYH", "UBT", "KZTR", "TGP", "SQDZDV", "AWEOYY", "NFJRXDX",
		"FYPTZF", "TIPOUZ", "NCNVK", "QJYBP", "MSD", "AHNMJ","DFPKE", "QME", "IGRO", "OSODH", "ULBOW", "FSZR", "INYG", 
		"OOVCAKX", "IRXNENL", "XODHACQ", "BNV", "MIG", "TJN", "UXNPNGN", "ACG", "UKBSOLN", "RFNAXV", "UHBLV", "ZVBYIQ",
		"GTV", "KACZOVS", "OKD", "CMD", "KFXB", "IHMBSHC", "BVJXFFJ", "YESJ", "VPWY", "GHINT", "MFBTOT", "EYMTHL", 
		"FQXKOUN", "LWK", "AMCYE", "SQEYSG", "KYCNW", "LVRNKS", "GMF", "SSET", "LHYVWCT", "ZAH", "QTK", "WVTYLN", 
		"UBOXTW", "ZQVAO", "WCW", "VKWQI", "KBUQJL", "VAK", "VBAEXUK", "TJZEJJV", "ROLQ", "GZT", "CQHZDXL", "YWYC",
		"ZUZLJFW", "XSFPXGC", "GDNXSLX", "XCZO", "RLEOBPJ", "CSNL", "VLUQ", "YLDLGBC","QZQP", "MKMFRTF", "LTJVFR", 
		"XIUUFDM", "ELCGHW", "DIDCRHK", "BNHJTT", "HZGXIPD", "MTINCH", "ZNMPPLY", "PRGADQ", "QQMXXKY", "JDPW", "YAJBA", 
		"YYR", "WLMZXR", "SDD", "FWEDTT", "GBNFDBY", "GMY","GTS", "KGENFAF", "OWX", "QCJOH", "OQWRSLO", "KBFTC", "ZSTPWS",
		"LYXTR", "TLXJ", "TRU", "LEZSTCZ", "OOKDIW", "UDEND", "LQCBM", "YLMGK", "NMQT", "GBU", "ZYU", "BGX", "NYHJCR", 
		"SDZTB", "KGAAQ", "VSQ", "XAKXC", "RFOJ", "BAFY", "ZWSRCQV", "XREUS", "HNER", "JQEV", "GMZZA", "KXHVZSI", "ZWD", 
		"IGSZ", "RXQXRQZ", "XZNNXBS", "RAHFOPI" , "MHAQ", "XMIPGJQ", "SQCOUP", "WID", "JSX", "HXYR", "BSXFL", "NKDC", 
		"NBRDGI", "YKX", "FIP", "TJAJ", "YQSUL", "TWPCTY", "HZCJBH", "HXL", "YYGC", "SVKZ", "RYJUR", "MMMUFBF", "PRWMMG",
		"HGTOHU", "XNV", "FCNKYNH", "AFFACVR", "XFKGRQI", "GVTUZHU", "WXFQ", "MLKPQBI", "KIAU", "HAHDH", "SZRT", "EZYN", 
		"ODK", "ABAPA", "HPVVWIY", "IZHGA", "ONNBJY", "KWTLPL", "XOMPR", "HGVPUH", "YBRA",
]


if __name__ == "__main__":
	print(compute())
