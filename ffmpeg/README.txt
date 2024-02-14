FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2024-02-04-git-7375a6ca7b-essentials_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/7375a6ca7b

git-essentials build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
3DNow! enabled            yes
3DNow! extended enabled   yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
EBP available             yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
postprocessing support    yes
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
xmllint enabled           yes

External libraries:
avisynth                libopencore_amrnb       libvpx
bzlib                   libopencore_amrwb       libwebp
gmp                     libopenjpeg             libx264
gnutls                  libopenmpt              libx265
iconv                   libopus                 libxml2
libaom                  librubberband           libxvid
libass                  libspeex                libzimg
libfontconfig           libsrt                  libzmq
libfreetype             libssh                  lzma
libfribidi              libtheora               mediafoundation
libgme                  libvidstab              sdl2
libgsm                  libvmaf                 zlib
libharfbuzz             libvo_amrwbenc
libmp3lame              libvorbis

External libraries providing hardware acceleration:
amf                     d3d11va                 libvpl
cuda                    dxva2                   nvdec
cuda_llvm               ffnvcodec               nvenc
cuvid                   libmfx

Libraries:
avcodec                 avformat                swresample
avdevice                avutil                  swscale
avfilter                postproc

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     fourxm                  pfm
aac_fixed               fraps                   pgm
aac_latm                frwu                    pgmyuv
aasc                    ftr                     pgssub
ac3                     g2m                     pgx
ac3_fixed               g723_1                  phm
acelp_kelvin            g729                    photocd
adpcm_4xm               gdv                     pictor
adpcm_adx               gem                     pixlet
adpcm_afc               gif                     pjs
adpcm_agm               gremlin_dpcm            png
adpcm_aica              gsm                     ppm
adpcm_argo              gsm_ms                  prores
adpcm_ct                h261                    prosumer
adpcm_dtk               h263                    psd
adpcm_ea                h263i                   ptx
adpcm_ea_maxis_xa       h263p                   qcelp
adpcm_ea_r1             h264                    qdm2
adpcm_ea_r2             h264_cuvid              qdmc
adpcm_ea_r3             h264_qsv                qdraw
adpcm_ea_xas            hap                     qoa
adpcm_g722              hca                     qoi
adpcm_g726              hcom                    qpeg
adpcm_g726le            hdr                     qtrle
adpcm_ima_acorn         hevc                    r10k
adpcm_ima_alp           hevc_cuvid              r210
adpcm_ima_amv           hevc_qsv                ra_144
adpcm_ima_apc           hnm4_video              ra_288
adpcm_ima_apm           hq_hqa                  ralf
adpcm_ima_cunning       hqx                     rasc
adpcm_ima_dat4          huffyuv                 rawvideo
adpcm_ima_dk3           hymt                    realtext
adpcm_ima_dk4           iac                     rka
adpcm_ima_ea_eacs       idcin                   rl2
adpcm_ima_ea_sead       idf                     roq
adpcm_ima_iss           iff_ilbm                roq_dpcm
adpcm_ima_moflex        ilbc                    rpza
adpcm_ima_mtf           imc                     rscc
adpcm_ima_oki           imm4                    rtv1
adpcm_ima_qt            imm5                    rv10
adpcm_ima_rad           indeo2                  rv20
adpcm_ima_smjpeg        indeo3                  rv30
adpcm_ima_ssi           indeo4                  rv40
adpcm_ima_wav           indeo5                  s302m
adpcm_ima_ws            interplay_acm           sami
adpcm_ms                interplay_dpcm          sanm
adpcm_mtaf              interplay_video         sbc
adpcm_psx               ipu                     scpr
adpcm_sbpro_2           jacosub                 screenpresso
adpcm_sbpro_3           jpeg2000                sdx2_dpcm
adpcm_sbpro_4           jpegls                  sga
adpcm_swf               jv                      sgi
adpcm_thp               kgv1                    sgirle
adpcm_thp_le            kmvc                    sheervideo
adpcm_vima              lagarith                shorten
adpcm_xa                lead                    simbiosis_imx
adpcm_xmd               libaom_av1              sipr
adpcm_yamaha            libgsm                  siren
adpcm_zork              libgsm_ms               smackaud
agm                     libopencore_amrnb       smacker
aic                     libopencore_amrwb       smc
alac                    libopus                 smvjpeg
alias_pix               libspeex                snow
als                     libvorbis               sol_dpcm
amrnb                   libvpx_vp8              sonic
amrwb                   libvpx_vp9              sp5x
amv                     loco                    speedhq
anm                     lscr                    speex
ansi                    m101                    srgc
anull                   mace3                   srt
apac                    mace6                   ssa
ape                     magicyuv                stl
apng                    mdec                    subrip
aptx                    media100                subviewer
aptx_hd                 metasound               subviewer1
arbc                    microdvd                sunrast
argo                    mimic                   svq1
ass                     misc4                   svq3
asv1                    mjpeg                   tak
asv2                    mjpeg_cuvid             targa
atrac1                  mjpeg_qsv               targa_y216
atrac3                  mjpegb                  tdsc
atrac3al                mlp                     text
atrac3p                 mmvideo                 theora
atrac3pal               mobiclip                thp
atrac9                  motionpixels            tiertexseqvideo
aura                    movtext                 tiff
aura2                   mp1                     tmv
av1                     mp1float                truehd
av1_cuvid               mp2                     truemotion1
av1_qsv                 mp2float                truemotion2
avrn                    mp3                     truemotion2rt
avrp                    mp3adu                  truespeech
avs                     mp3adufloat             tscc
avui                    mp3float                tscc2
ayuv                    mp3on4                  tta
bethsoftvid             mp3on4float             twinvq
bfi                     mpc7                    txd
bink                    mpc8                    ulti
binkaudio_dct           mpeg1_cuvid             utvideo
binkaudio_rdft          mpeg1video              v210
bintext                 mpeg2_cuvid             v210x
bitpacked               mpeg2_qsv               v308
bmp                     mpeg2video              v408
bmv_audio               mpeg4                   v410
bmv_video               mpeg4_cuvid             vb
bonk                    mpegvideo               vble
brender_pix             mpl2                    vbn
c93                     msa1                    vc1
cavs                    mscc                    vc1_cuvid
cbd2_dpcm               msmpeg4v1               vc1_qsv
ccaption                msmpeg4v2               vc1image
cdgraphics              msmpeg4v3               vcr1
cdtoons                 msnsiren                vmdaudio
cdxl                    msp2                    vmdvideo
cfhd                    msrle                   vmix
cinepak                 mss1                    vmnc
clearvideo              mss2                    vnull
cljr                    msvideo1                vorbis
cllc                    mszh                    vp3
comfortnoise            mts2                    vp4
cook                    mv30                    vp5
cpia                    mvc1                    vp6
cri                     mvc2                    vp6a
cscd                    mvdv                    vp6f
cyuv                    mvha                    vp7
dca                     mwsc                    vp8
dds                     mxpeg                   vp8_cuvid
derf_dpcm               nellymoser              vp8_qsv
dfa                     notchlc                 vp9
dfpwm                   nuv                     vp9_cuvid
dirac                   on2avc                  vp9_qsv
dnxhd                   opus                    vplayer
dolby_e                 osq                     vqa
dpx                     paf_audio               vqc
dsd_lsbf                paf_video               vvc
dsd_lsbf_planar         pam                     wady_dpcm
dsd_msbf                pbm                     wavarc
dsd_msbf_planar         pcm_alaw                wavpack
dsicinaudio             pcm_bluray              wbmp
dsicinvideo             pcm_dvd                 wcmv
dss_sp                  pcm_f16le               webp
dst                     pcm_f24le               webvtt
dvaudio                 pcm_f32be               wmalossless
dvbsub                  pcm_f32le               wmapro
dvdsub                  pcm_f64be               wmav1
dvvideo                 pcm_f64le               wmav2
dxa                     pcm_lxf                 wmavoice
dxtory                  pcm_mulaw               wmv1
dxv                     pcm_s16be               wmv2
eac3                    pcm_s16be_planar        wmv3
eacmv                   pcm_s16le               wmv3image
eamad                   pcm_s16le_planar        wnv1
eatgq                   pcm_s24be               wrapped_avframe
eatgv                   pcm_s24daud             ws_snd1
eatqi                   pcm_s24le               xan_dpcm
eightbps                pcm_s24le_planar        xan_wc3
eightsvx_exp            pcm_s32be               xan_wc4
eightsvx_fib            pcm_s32le               xbin
escape124               pcm_s32le_planar        xbm
escape130               pcm_s64be               xface
evrc                    pcm_s64le               xl
exr                     pcm_s8                  xma1
fastaudio               pcm_s8_planar           xma2
ffv1                    pcm_sga                 xpm
ffvhuff                 pcm_u16be               xsub
ffwavesynth             pcm_u16le               xwd
fic                     pcm_u24be               y41p
fits                    pcm_u24le               ylc
flac                    pcm_u32be               yop
flashsv                 pcm_u32le               yuv4
flashsv2                pcm_u8                  zero12v
flic                    pcm_vidc                zerocodec
flv                     pcx                     zlib
fmvc                    pdv                     zmbv

Enabled encoders:
a64multi                hevc_mf                 pcm_u24le
a64multi5               hevc_nvenc              pcm_u32be
aac                     hevc_qsv                pcm_u32le
aac_mf                  huffyuv                 pcm_u8
ac3                     jpeg2000                pcm_vidc
ac3_fixed               jpegls                  pcx
ac3_mf                  libaom_av1              pfm
adpcm_adx               libgsm                  pgm
adpcm_argo              libgsm_ms               pgmyuv
adpcm_g722              libmp3lame              phm
adpcm_g726              libopencore_amrnb       png
adpcm_g726le            libopenjpeg             ppm
adpcm_ima_alp           libopus                 prores
adpcm_ima_amv           libspeex                prores_aw
adpcm_ima_apm           libtheora               prores_ks
adpcm_ima_qt            libvo_amrwbenc          qoi
adpcm_ima_ssi           libvorbis               qtrle
adpcm_ima_wav           libvpx_vp8              r10k
adpcm_ima_ws            libvpx_vp9              r210
adpcm_ms                libwebp                 ra_144
adpcm_swf               libwebp_anim            rawvideo
adpcm_yamaha            libx264                 roq
alac                    libx264rgb              roq_dpcm
alias_pix               libx265                 rpza
amv                     libxvid                 rv10
anull                   ljpeg                   rv20
apng                    magicyuv                s302m
aptx                    mjpeg                   sbc
aptx_hd                 mjpeg_qsv               sgi
ass                     mlp                     smc
asv1                    movtext                 snow
asv2                    mp2                     sonic
av1_amf                 mp2fixed                sonic_ls
av1_nvenc               mp3_mf                  speedhq
av1_qsv                 mpeg1video              srt
avrp                    mpeg2_qsv               ssa
avui                    mpeg2video              subrip
ayuv                    mpeg4                   sunrast
bitpacked               msmpeg4v2               svq1
bmp                     msmpeg4v3               targa
cfhd                    msrle                   text
cinepak                 msvideo1                tiff
cljr                    nellymoser              truehd
comfortnoise            opus                    tta
dca                     pam                     ttml
dfpwm                   pbm                     utvideo
dnxhd                   pcm_alaw                v210
dpx                     pcm_bluray              v308
dvbsub                  pcm_dvd                 v408
dvdsub                  pcm_f32be               v410
dvvideo                 pcm_f32le               vbn
dxv                     pcm_f64be               vc2
eac3                    pcm_f64le               vnull
exr                     pcm_mulaw               vorbis
ffv1                    pcm_s16be               vp9_qsv
ffvhuff                 pcm_s16be_planar        wavpack
fits                    pcm_s16le               wbmp
flac                    pcm_s16le_planar        webvtt
flashsv                 pcm_s24be               wmav1
flashsv2                pcm_s24daud             wmav2
flv                     pcm_s24le               wmv1
g723_1                  pcm_s24le_planar        wmv2
gif                     pcm_s32be               wrapped_avframe
h261                    pcm_s32le               xbm
h263                    pcm_s32le_planar        xface
h263p                   pcm_s64be               xsub
h264_amf                pcm_s64le               xwd
h264_mf                 pcm_s8                  y41p
h264_nvenc              pcm_s8_planar           yuv4
h264_qsv                pcm_u16be               zlib
hdr                     pcm_u16le               zmbv
hevc_amf                pcm_u24be

Enabled hwaccels:
av1_d3d11va             hevc_nvdec              vc1_nvdec
av1_d3d11va2            mjpeg_nvdec             vp8_nvdec
av1_dxva2               mpeg1_nvdec             vp9_d3d11va
av1_nvdec               mpeg2_d3d11va           vp9_d3d11va2
h264_d3d11va            mpeg2_d3d11va2          vp9_dxva2
h264_d3d11va2           mpeg2_dxva2             vp9_nvdec
h264_dxva2              mpeg2_nvdec             wmv3_d3d11va
h264_nvdec              mpeg4_nvdec             wmv3_d3d11va2
hevc_d3d11va            vc1_d3d11va             wmv3_dxva2
hevc_d3d11va2           vc1_d3d11va2            wmv3_nvdec
hevc_dxva2              vc1_dxva2

Enabled parsers:
aac                     dvdsub                  mpegaudio
aac_latm                evc                     mpegvideo
ac3                     flac                    opus
adx                     ftr                     png
amr                     g723_1                  pnm
av1                     g729                    qoi
avs2                    gif                     rv34
avs3                    gsm                     sbc
bmp                     h261                    sipr
cavsvideo               h263                    tak
cook                    h264                    vc1
cri                     hdr                     vorbis
dca                     hevc                    vp3
dirac                   ipu                     vp8
dnxhd                   jpeg2000                vp9
dolby_e                 jpegxl                  vvc
dpx                     misc4                   webp
dvaudio                 mjpeg                   xbm
dvbsub                  mlp                     xma
dvd_nav                 mpeg4video              xwd

Enabled demuxers:
aa                      idcin                   pcm_f64le
aac                     idf                     pcm_mulaw
aax                     iff                     pcm_s16be
ac3                     ifv                     pcm_s16le
ac4                     ilbc                    pcm_s24be
ace                     image2                  pcm_s24le
acm                     image2_alias_pix        pcm_s32be
act                     image2_brender_pix      pcm_s32le
adf                     image2pipe              pcm_s8
adp                     image_bmp_pipe          pcm_u16be
ads                     image_cri_pipe          pcm_u16le
adx                     image_dds_pipe          pcm_u24be
aea                     image_dpx_pipe          pcm_u24le
afc                     image_exr_pipe          pcm_u32be
aiff                    image_gem_pipe          pcm_u32le
aix                     image_gif_pipe          pcm_u8
alp                     image_hdr_pipe          pcm_vidc
amr                     image_j2k_pipe          pdv
amrnb                   image_jpeg_pipe         pjs
amrwb                   image_jpegls_pipe       pmp
anm                     image_jpegxl_pipe       pp_bnk
apac                    image_pam_pipe          pva
apc                     image_pbm_pipe          pvf
ape                     image_pcx_pipe          qcp
apm                     image_pfm_pipe          qoa
apng                    image_pgm_pipe          r3d
aptx                    image_pgmyuv_pipe       rawvideo
aptx_hd                 image_pgx_pipe          realtext
aqtitle                 image_phm_pipe          redspark
argo_asf                image_photocd_pipe      rka
argo_brp                image_pictor_pipe       rl2
argo_cvg                image_png_pipe          rm
asf                     image_ppm_pipe          roq
asf_o                   image_psd_pipe          rpl
ass                     image_qdraw_pipe        rsd
ast                     image_qoi_pipe          rso
au                      image_sgi_pipe          rtp
av1                     image_sunrast_pipe      rtsp
avi                     image_svg_pipe          s337m
avisynth                image_tiff_pipe         sami
avr                     image_vbn_pipe          sap
avs                     image_webp_pipe         sbc
avs2                    image_xbm_pipe          sbg
avs3                    image_xpm_pipe          scc
bethsoftvid             image_xwd_pipe          scd
bfi                     imf                     sdns
bfstm                   ingenient               sdp
bink                    ipmovie                 sdr2
binka                   ipu                     sds
bintext                 ircam                   sdx
bit                     iss                     segafilm
bitpacked               iv8                     ser
bmv                     ivf                     sga
boa                     ivr                     shorten
bonk                    jacosub                 siff
brstm                   jpegxl_anim             simbiosis_imx
c93                     jv                      sln
caf                     kux                     smacker
cavsvideo               kvag                    smjpeg
cdg                     laf                     smush
cdxl                    libgme                  sol
cine                    libopenmpt              sox
codec2                  live_flv                spdif
codec2raw               lmlm4                   srt
concat                  loas                    stl
dash                    lrc                     str
data                    luodat                  subviewer
daud                    lvf                     subviewer1
dcstr                   lxf                     sup
derf                    m4v                     svag
dfa                     matroska                svs
dfpwm                   mca                     swf
dhav                    mcc                     tak
dirac                   mgsts                   tedcaptions
dnxhd                   microdvd                thp
dsf                     mjpeg                   threedostr
dsicin                  mjpeg_2000              tiertexseq
dss                     mlp                     tmv
dts                     mlv                     truehd
dtshd                   mm                      tta
dv                      mmf                     tty
dvbsub                  mods                    txd
dvbtxt                  moflex                  ty
dxa                     mov                     usm
ea                      mp3                     v210
ea_cdata                mpc                     v210x
eac3                    mpc8                    vag
epaf                    mpegps                  vc1
evc                     mpegts                  vc1t
ffmetadata              mpegtsraw               vividas
filmstrip               mpegvideo               vivo
fits                    mpjpeg                  vmd
flac                    mpl2                    vobsub
flic                    mpsub                   voc
flv                     msf                     vpk
fourxm                  msnwc_tcp               vplayer
frm                     msp                     vqf
fsb                     mtaf                    vvc
fwse                    mtv                     w64
g722                    musx                    wady
g723_1                  mv                      wav
g726                    mvi                     wavarc
g726le                  mxf                     wc3
g729                    mxg                     webm_dash_manifest
gdv                     nc                      webvtt
genh                    nistsphere              wsaud
gif                     nsp                     wsd
gsm                     nsv                     wsvqa
gxf                     nut                     wtv
h261                    nuv                     wv
h263                    obu                     wve
h264                    ogg                     xa
hca                     oma                     xbin
hcom                    osq                     xmd
hevc                    paf                     xmv
hls                     pcm_alaw                xvag
hnm                     pcm_f32be               xwma
iamf                    pcm_f32le               yop
ico                     pcm_f64be               yuv4mpegpipe

Enabled muxers:
a64                     h263                    pcm_s24be
ac3                     h264                    pcm_s24le
ac4                     hash                    pcm_s32be
adts                    hds                     pcm_s32le
adx                     hevc                    pcm_s8
aiff                    hls                     pcm_u16be
alp                     iamf                    pcm_u16le
amr                     ico                     pcm_u24be
amv                     ilbc                    pcm_u24le
apm                     image2                  pcm_u32be
apng                    image2pipe              pcm_u32le
aptx                    ipod                    pcm_u8
aptx_hd                 ircam                   pcm_vidc
argo_asf                ismv                    psp
argo_cvg                ivf                     rawvideo
asf                     jacosub                 rcwt
asf_stream              kvag                    rm
ass                     latm                    roq
ast                     lrc                     rso
au                      m4v                     rtp
avi                     matroska                rtp_mpegts
avif                    matroska_audio          rtsp
avm2                    md5                     sap
avs2                    microdvd                sbc
avs3                    mjpeg                   scc
bit                     mkvtimestamp_v2         segafilm
caf                     mlp                     segment
cavsvideo               mmf                     smjpeg
codec2                  mov                     smoothstreaming
codec2raw               mp2                     sox
crc                     mp3                     spdif
dash                    mp4                     spx
data                    mpeg1system             srt
daud                    mpeg1vcd                stream_segment
dfpwm                   mpeg1video              streamhash
dirac                   mpeg2dvd                sup
dnxhd                   mpeg2svcd               swf
dts                     mpeg2video              tee
dv                      mpeg2vob                tg2
eac3                    mpegts                  tgp
evc                     mpjpeg                  truehd
f4v                     mxf                     tta
ffmetadata              mxf_d10                 ttml
fifo                    mxf_opatom              uncodedframecrc
fifo_test               null                    vc1
filmstrip               nut                     vc1t
fits                    obu                     voc
flac                    oga                     vvc
flv                     ogg                     w64
framecrc                ogv                     wav
framehash               oma                     webm
framemd5                opus                    webm_chunk
g722                    pcm_alaw                webm_dash_manifest
g723_1                  pcm_f32be               webp
g726                    pcm_f32le               webvtt
g726le                  pcm_f64be               wsaud
gif                     pcm_f64le               wtv
gsm                     pcm_mulaw               wv
gxf                     pcm_s16be               yuv4mpegpipe
h261                    pcm_s16le

Enabled protocols:
async                   http                    rtmp
cache                   httpproxy               rtmpe
concat                  https                   rtmps
concatf                 icecast                 rtmpt
crypto                  ipfs_gateway            rtmpte
data                    ipns_gateway            rtmpts
fd                      libsrt                  rtp
ffrtmpcrypt             libssh                  srtp
ffrtmphttp              libzmq                  subfile
file                    md5                     tcp
ftp                     mmsh                    tee
gopher                  mmst                    tls
gophers                 pipe                    udp
hls                     prompeg                 udplite

Enabled filters:
a3dscope                crossfeed               owdenoise
aap                     crystalizer             pad
abench                  cue                     pal100bars
abitscope               curves                  pal75bars
acompressor             datascope               palettegen
acontrast               dblur                   paletteuse
acopy                   dcshift                 pan
acrossfade              dctdnoiz                perms
acrossover              ddagrab                 perspective
acrusher                deband                  phase
acue                    deblock                 photosensitivity
addroi                  decimate                pixdesctest
adeclick                deconvolve              pixelize
adeclip                 dedot                   pixscope
adecorrelate            deesser                 pp
adelay                  deflate                 pp7
adenorm                 deflicker               premultiply
aderivative             deinterlace_qsv         prewitt
adrawgraph              dejudder                pseudocolor
adrc                    delogo                  psnr
adynamicequalizer       derain                  pullup
adynamicsmooth          deshake                 qp
aecho                   despill                 random
aemphasis               detelecine              readeia608
aeval                   dialoguenhance          readvitc
aevalsrc                dilation                realtime
aexciter                displace                remap
afade                   dnn_classify            removegrain
afdelaysrc              dnn_detect              removelogo
afftdn                  dnn_processing          repeatfields
afftfilt                doubleweave             replaygain
afifo                   drawbox                 reverse
afir                    drawgraph               rgbashift
afireqsrc               drawgrid                rgbtestsrc
afirsrc                 drawtext                roberts
aformat                 drmeter                 rotate
afreqshift              dynaudnorm              rubberband
afwtdn                  earwax                  sab
agate                   ebur128                 scale
agraphmonitor           edgedetect              scale2ref
ahistogram              elbg                    scale_cuda
aiir                    entropy                 scale_qsv
aintegral               epx                     scdet
ainterleave             eq                      scharr
alatency                equalizer               scroll
alimiter                erosion                 segment
allpass                 estdif                  select
allrgb                  exposure                selectivecolor
allyuv                  extractplanes           sendcmd
aloop                   extrastereo             separatefields
alphaextract            fade                    setdar
alphamerge              feedback                setfield
amerge                  fftdnoiz                setparams
ametadata               fftfilt                 setpts
amix                    field                   setrange
amovie                  fieldhint               setsar
amplify                 fieldmatch              settb
amultiply               fieldorder              shear
anequalizer             fifo                    showcqt
anlmdn                  fillborders             showcwt
anlmf                   find_rect               showfreqs
anlms                   firequalizer            showinfo
anoisesrc               flanger                 showpalette
anull                   floodfill               showspatial
anullsink               format                  showspectrum
anullsrc                fps                     showspectrumpic
apad                    framepack               showvolume
aperms                  framerate               showwaves
aphasemeter             framestep               showwavespic
aphaser                 freezedetect            shuffleframes
aphaseshift             freezeframes            shufflepixels
apsnr                   fspp                    shuffleplanes
apsyclip                fsync                   sidechaincompress
apulsator               gblur                   sidechaingate
arealtime               geq                     sidedata
aresample               gradfun                 sierpinski
areverse                gradients               signalstats
arls                    graphmonitor            signature
arnndn                  grayworld               silencedetect
asdr                    greyedge                silenceremove
asegment                guided                  sinc
aselect                 haas                    sine
asendcmd                haldclut                siti
asetnsamples            haldclutsrc             smartblur
asetpts                 hdcd                    smptebars
asetrate                headphone               smptehdbars
asettb                  hflip                   sobel
ashowinfo               highpass                spectrumsynth
asidedata               highshelf               speechnorm
asisdr                  hilbert                 split
asoftclip               histeq                  spp
aspectralstats          histogram               sr
asplit                  hqdn3d                  ssim
ass                     hqx                     ssim360
astats                  hstack                  stereo3d
astreamselect           hstack_qsv              stereotools
asubboost               hsvhold                 stereowiden
asubcut                 hsvkey                  streamselect
asupercut               hue                     subtitles
asuperpass              huesaturation           super2xsai
asuperstop              hwdownload              superequalizer
atadenoise              hwmap                   surround
atempo                  hwupload                swaprect
atilt                   hwupload_cuda           swapuv
atrim                   hysteresis              tblend
avectorscope            identity                telecine
avgblur                 idet                    testsrc
avsynctest              il                      testsrc2
axcorrelate             inflate                 thistogram
azmq                    interlace               threshold
backgroundkey           interleave              thumbnail
bandpass                join                    thumbnail_cuda
bandreject              kerndeint               tile
bass                    kirsch                  tiltandshift
bbox                    lagfun                  tiltshelf
bench                   latency                 tinterlace
bilateral               lenscorrection          tlut2
bilateral_cuda          libvmaf                 tmedian
biquad                  life                    tmidequalizer
bitplanenoise           limitdiff               tmix
blackdetect             limiter                 tonemap
blackframe              loop                    tpad
blend                   loudnorm                transpose
blockdetect             lowpass                 treble
blurdetect              lowshelf                tremolo
bm3d                    lumakey                 trim
boxblur                 lut                     unpremultiply
bwdif                   lut1d                   unsharp
bwdif_cuda              lut2                    untile
cas                     lut3d                   uspp
ccrepack                lutrgb                  v360
cellauto                lutyuv                  vaguedenoiser
channelmap              mandelbrot              varblur
channelsplit            maskedclamp             vectorscope
chorus                  maskedmax               vflip
chromahold              maskedmerge             vfrdet
chromakey               maskedmin               vibrance
chromakey_cuda          maskedthreshold         vibrato
chromanr                maskfun                 vidstabdetect
chromashift             mcdeint                 vidstabtransform
ciescope                mcompand                vif
codecview               median                  vignette
color                   mergeplanes             virtualbass
colorbalance            mestimate               vmafmotion
colorchannelmixer       metadata                volume
colorchart              midequalizer            volumedetect
colorcontrast           minterpolate            vpp_qsv
colorcorrect            mix                     vstack
colorhold               monochrome              vstack_qsv
colorize                morpho                  w3fdif
colorkey                movie                   waveform
colorlevels             mpdecimate              weave
colormap                mptestsrc               xbr
colormatrix             msad                    xcorrelate
colorspace              multiply                xfade
colorspace_cuda         negate                  xmedian
colorspectrum           nlmeans                 xstack
colortemperature        nnedi                   xstack_qsv
compand                 noformat                yadif
compensationdelay       noise                   yadif_cuda
concat                  normalize               yaepblur
convolution             null                    yuvtestsrc
convolve                nullsink                zmq
copy                    nullsrc                 zoneplate
corr                    oscilloscope            zoompan
cover_rect              overlay                 zscale
crop                    overlay_cuda
cropdetect              overlay_qsv

Enabled bsfs:
aac_adtstoasc           h264_redundant_pps      pcm_rechunk
av1_frame_merge         hapqa_extract           pgs_frame_merge
av1_frame_split         hevc_metadata           prores_metadata
av1_metadata            hevc_mp4toannexb        remove_extradata
chomp                   imx_dump_header         setts
dca_core                media100_to_mjpegb      showinfo
dts2pts                 mjpeg2jpeg              text2movsub
dump_extradata          mjpega_dump_header      trace_headers
dv_error_marker         mov2textsub             truehd_core
eac3_core               mp3_header_decompress   vp9_metadata
evc_frame_merge         mpeg2_metadata          vp9_raw_reorder
extract_extradata       mpeg4_unpack_bframes    vp9_superframe
filter_units            noise                   vp9_superframe_split
h264_metadata           null                    vvc_metadata
h264_mp4toannexb        opus_metadata           vvc_mp4toannexb

Enabled indevs:
dshow                   lavfi
gdigrab                 vfwcap

Enabled outdevs:
sdl2

git-essentials external libraries' versions: 

AMF v1.4.32-2-g8787d3e
aom v3.8.1-258-g498e799b8f
AviSynthPlus v3.7.3-63-g9bd6fcca
ffnvcodec n12.1.14.0-1-g75f032b
freetype VER-2-13-2
fribidi v1.0.13-2-g5b9a242
gsm 1.0.22
harfbuzz 8.3.0-85-ga9b889179
lame 3.100
libass 0.17.0-71-g58a8f09
libgme 0.6.3
libopencore-amrnb 0.1.6
libopencore-amrwb 0.1.6
libssh 0.10.4
libtheora 1.1.1
libwebp v1.3.2-111-gf99305e9
oneVPL 2.9
openmpt libopenmpt-0.6.12-72-gc35f5bb36
rubberband v1.8.1
SDL prerelease-2.29.2-39-gc53c35192
speex Speex-1.2.1-20-g3693431
srt v1.5.3-34-g4c443d6
vidstab v1.1.1-11-gc8caf90
vmaf v3.0.0-45-g346e176d
vo-amrwbenc 0.1.3
vorbis v1.3.7-10-g84c02369
vpx v1.14.0-99-ga9bd789d2
x264 v0.164.3173
x265 3.5-155-g74abf80c7
xvid v1.3.7
zeromq 4.3.5
zimg release-3.0.5-150-g7143181

