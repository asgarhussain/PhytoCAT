import email
from unicodedata import name
from flask import Flask, render_template,request,g,flash,redirect,url_for,jsonify,session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, TextAreaField, RadioField, SelectField,TextField,validators
from wtforms.validators import InputRequired,Length,AnyOf,ValidationError,NoneOf,Regexp,Email
from wtforms.fields.html5 import EmailField

from matplotlib import pyplot as plt              
from subprocess	import	call
from flask import send_file
import datetime

import subprocess
import sys
import re
import numpy as np
from io import BytesIO
import base64
import os
import time
import ntpath
import pandas as pd
import sqlite3
import random
from matplotlib.pyplot import figure

app = Flask(__name__)
app.config['SECRET_KEY'] = '!'

def connect_db():

    #sql=sqlite3.connect('/home/igib/Phytocat/phytocatdb/db/phyto_chemicals.db') ###change the directory accordingly
    sql=sqlite3.connect('./db/phyto_chemicals_300524.db') ###change the directory accordingly
    #sql=sqlite3.connect('/home/anuvanshiki/firdaus/updated/Phytocat/phytocatdb/db/phyto_chemicals_28dec.db') ###change the directory accordingly

 
    sql.row_factory=sqlite3.Row
    return sql
def get_db():
    if not hasattr (g,'sqlite3'):
        g.sqlite_db=connect_db()
    return g.sqlite_db        

@app.teardown_appcontext
def close_db(error):
    if hasattr (g,'sqlite_db'):
        g.sqlite_db.close()


def Convert(string):
    li = list(string.split("|"))
    return li


     

class MyForm(FlaskForm):
    Phytochemical = TextAreaField('Phytochemical', validators=[ InputRequired()  ] ) 

class MLP(FlaskForm):
    MLP = TextAreaField('MLP', validators=[ InputRequired()  ] ) 


class Plants(FlaskForm):
    Plant = TextAreaField('Plant', validators=[ InputRequired()  ] )     


class Genes(FlaskForm):
    Gene = TextAreaField('Gene', validators=[ InputRequired()  ] )     

#class alphabatical(FlaskForm):
#    alphabatical = TextAreaField('alphabatical', validators=[ InputRequired()  ] )     


class contactus(FlaskForm):

    name = StringField('Name',validators=[InputRequired(),validators.length(min=4, max=25)]   )
    email = EmailField('Email', validators=[InputRequired(),validators.Email(),Email()])
    organization = TextAreaField('Organization', validators=[InputRequired(), validators.Length(min=3, max=100)]   )
    suggestions = TextAreaField('Suggestions', validators=[InputRequired(), validators.Length(max=300)])


@app.route('/',  methods=['GET', 'POST'])
def index():

    #global counter
    #counter += 1
    db=get_db()
    form = MLP()
    #form = MyForm()
    if request.method == 'POST' :
        #rsid1=request.form['RSID']
        Phytochemical=form.MLP.data
        #return render_template()
        #return '<h1>RSID:{}'.format(rsid1)
        print ("Phytochemical ::::")
        #print(Phytochemical)
        pat = re.compile('Alkaloid|Sesquiterpene lactone|Coumarin|Terpenoid|Flav|Essential oil|extract|Saponin|Triterpenoid saponin|Lignan|Quinone|Xanthone')
        pl_list=['Abies fargesii', 'Abutilon theophrasti', 'Acacia carneorum\nAcacia buxifolia', 'Acacia catechu', 'Acacia cyclops', 'Acacia etbaica', 'Acacia retinodes', 'Acacia victoriae', 'Acalypha fruticosa Forssk', 'Acer palmatum', 'Acer rubrum', 'Achyranthes bidentata Blume', 'Achyranthes fauriei', 'Achyrocline satureioides', 'Acokanthera oppositifolia, Acokanthera schimperi', 'Aconitum barbatum\nAconitum napellus\nAconitum yesoense', 'Aconitum sinchiangense', 'Acridocarpus orientalis', 'Actaea racemosa', 'Actinidia chinensis', 'Actinocephalus divaricatus', 'Actinostemma lobatum', 'Adenium obesum', 'Adiantum capillus', 'Adinandra nitida', 'Adonis multiflora Nishikawa & Koki Ito', 'Adonis multiflora, Tupistra chinensis', 'Aegle marmelos', 'Aeollanthus rydingianus', 'Aesculus chinensis', 'Aesculus hippocastanum', 'Agaricus albus', 'Agaricus bisporous', 'Agaricus bisporous,Momordica charantia', 'Agave americana', 'Ageratum conyzoides', 'Aglaia abbreviata', 'Aglaia angustifolia', 'Aglaia crassinervia', 'Aglaia foveolata', 'Aglaia odorata', 'Agrimonia pilosa', 'Ailanthus altissima', 'Ajuga bracteosa', 'Ajuga chamaecistus', 'Albatrellus confluens', 'Albizia julibrissin', 'Albizzia julibrissin Durazz', 'Alisma canaliculatum', 'Alisma plantago-aquatica', 'Allium atroviolaceum', 'Allium autumnale', 'Allium bakhtiaricum', 'Allium cepa', 'Allium hirtifolium', 'Allium sativum', 'Allium sivasicum', 'Allium tuberosum', 'Allium vineale', 'Aloe perryi', 'Aloe vera', 'Alpinia conchigera', 'Alpinia galanga', 'Alpinia katsumadai', 'Alpinia mutica', 'Alpinia nantoensis', 'Alpinia officinarum', 'Alpinia oxyphylla', 'Alpinia pahangensis', 'Alseodaphne semecarpifolia', 'Alternaria alternata, an endophyte isolated from Paeonia lactiflora.', 'Alysicarpus vaginalis', 'Amaranthus cruentus', 'American ginseng', 'Ammopiptanthus mongolicus', 'Amomum subulatum', 'Amoora chittagonga', 'Amoora rohituka', 'Amorphophallus konjac\n Amorphophallus rivieri\n Amorphophallus sinensis', 'Amorphophallus paeoniifolius', 'Ampelopsis grossedentata', 'Ampelozizyphus amazonicus', 'Ampelozizyphus amazonicus Ducke', 'Anacardium occidentale', 'Ananas comosus', 'Anaphalis busua', 'Anastatica hierochuntica (L)', 'Andrographis paniculata', 'Androsace umbellata', 'Anemarrhena asphodeloidea Bunge', 'Anemone cylindrica', 'Anemopsis californica', 'Angelica amurensis', 'Angelica japonica', 'Angelica sinensis', 'Aniba heringeri', 'Anisomeles indica', 'Annona cherimola', 'Annona cherimolia', 'Annona glabra', 'Annona muricata', 'Annona muricata (Graviola)', 'Annona senegalensis', 'Annona squamosa', 'Anoectochilus formosanus Hayata', 'Antiaris toxicaria', 'Antrodia camphorata', 'Antrodia camphorata, Antrodia cinnamomea', 'Antrodia cinnamomea', 'Apodytes dimidiata', 'Arabidopsis thaliana', 'Arachis hypogaea', 'Arctium lappa', 'Ardisia Crenata', 'Ardisia colorata', 'Ardisia crenata', 'Ardisia gigantifolia', 'Ardisia virens', 'Areca catechu', 'Arisaema franchetianum Engl , citrus fruits (lemons, oranges, tangerines, and grapefruits)', 'Arisaema tortuosum', 'Aristolochia foetida', 'Armoracia rusticana', 'Aronia melanocarpa', 'Artabotrys hainanensis', 'Artabotrys hongkongensis', 'Artemisia Capillaris', 'Artemisia Keiskeana', 'Artemisia Selengensis', 'Artemisia Stolonifera', 'Artemisia absinthium', 'Artemisia annua', 'Artemisia biennis', 'Artemisia capillaris', 'Artemisia ciniformis', 'Artemisia diffusa', 'Artemisia herba', 'Artemisia herba alba', 'Artemisia indica', 'Artemisia monosperma', 'Artemisia persica', 'Artemisia princeps', 'Artemisia santolina', 'Artemisia vulgaris', 'Artocarpus elasticus', 'Artocarpus heterophyllus', 'Artocarpus lakoocha Wall ex', 'Artocarpus obtusus', 'Arundo donax', 'Aspergillus', 'Aspergillus fumigatus', 'Aspergillus ustus 094102', 'Asphodelus microcarpus', 'Aster poliothamnus', 'Astragali radix', 'Astragaloside IV - Astragalus membranaceus, \nα-solanine -  Solanum nigruminn, \nneferine - otus plumule, and \n2,3,5,6-tetramethylpyrazine -igusticum', 'Astragalus membranaceus', 'Atractylodes lancea', 'Aucklandia lappa', 'Avena sativa', 'Avicennia marina', 'Azadirachta indica', 'Bacopa monnieri', 'Baeckea frutescens', 'Baphicacanthus cusia', 'Bauhinia variegata', 'Beilschmiedia kunstleri', 'Berberidaceae, Magnoliaceae, Menispermaceae, or Papaveraceae botanical families\nBerberis cretica', 'Berberis amurensis', 'Berberis tsarica', 'Berberis vulgaris', 'Bergera koenigii', 'Berrywood tree, Asparagus cochinchinensis', 'Beta vulgaris', 'Biebersteinia multifida', 'Black cohosh', 'Black ginseng', 'Black tea', 'Boehmeria siamensis', 'Boerhaavia diffusa', 'Boesenbergia rotunda', 'Bolbostemma paniculatum', 'Bolbostemma paniculatum (Maxim) Franquet', 'Boletus edulis', 'Boswellia carteri', 'Boswellia frereana', 'Boswellia ovalifoliolata', 'Boswellia thurifera', 'Bouea macrophylla', 'Brassica carinata', 'Brassica nigra', 'Brassica oleracea', 'Broussonetia papyrifera', 'Brown algae', 'Brucea javanica', 'Bryonia dioica Jacq', 'Bryonia multiflora', 'Buddleja davidii', 'Bupleurum chinense', 'Bupleurum falcatum', 'Bupleurum marginatum', 'Bursera copallifera', 'Butea monosperma', 'Buxus microphylla', 'Caesalpinia minax', 'Caesalpinia sappan', 'Caesalpinia sappan.', 'Caesalpinia spinosa', 'Cajanus cajan', 'Calanticaria bicolor', 'Calcarisporium arbuscular', 'Calea urticifolia', 'Calendula arvensis', 'Callicarpa nudiflora', 'Calligonum polygonoides', 'Callistemon citrinus', 'Callistemon viminalis', 'Calophyllum inophyllum', 'Calotropis procera', 'Camellia oleifera', 'Camellia sinensis', 'Candelaria concolor lichen', 'Cannabis sativa', 'Capsicum annuum', 'Capsicum annuum.\nZingiber officinale Roscoe', 'Caralluma retrospiciens', 'Caralluma tuberculata', 'Carica papaya', 'Carpesium abrotanoides', 'Carrichtera annua', 'Carthamus tinctorius', 'Casearia sylvestris', 'Cassia alata', 'Cassia glauca', 'Cassia petersiana', 'Castanea sativa', 'Catha edulis', 'Catharanthus roseus', 'Celastrus hindsii', 'Celastrus paniculatus', 'Celosia argentea', 'Centaurea aegyptiaca', 'Centaurea bruguierana', 'Centaurea cyanus', 'Centaurea diluta\nArtemisia artica', 'Centaurea schmidii', 'Centella asiatica', 'Centipeda minima', 'Cephalanceropsis gracilis', 'Cephalantheropsis gracilis', 'Cephalotaxus harringtonia', 'Ceriops tagal', 'Cetraria islandica', 'Chaerophyllum aureum', 'Chaetomium longirostre', 'Chamaecyparis obtusa', 'Chelidonium majus', 'Chimonanthus nitens', 'Chimonanthus nitens Oliv', 'Chinese herb', 'Chisocheton tomentosus', 'Chloranthus anhuiensis', 'Chlorella minutissima', 'Christia vespertilionis', 'Chrysophthalmum montanum', 'Cicer arietinum', 'Cichorium Pumilum', 'Cichorium intybus', 'Cimicifuga dahurica (Turcz.) Maxim.', 'Cimicifuga foetida', 'Cimicifuga racemosa', 'Cimicifuga yunnanensis', 'Cinnamomum cassia', 'Cinnamomum cassia Blume', 'Cipura paludosa', 'Cirsium chanroenicum', 'Cirsium japonicum', 'Cirsium palustre', 'Cirsium rivulare', 'Citrullus lanatus', 'Citrus aurantifolia', 'Citrus hystrix', 'Citrus hystrix\nGarcinia penangiana\nDecaschistia parviflora', 'Citrus latipes', 'Citrus limetta', 'Citrus limon', 'Citrus plant', 'Citrus sinensis', 'Citrus sphaerocarpa', 'Citrus tankan', 'Cladonia convolute', 'Cladonia rangiformis', 'Cladosporium cladosporioides', 'Cladosporium oxysporum', 'Clausena excavata Burm', 'Clausena hainanensis', 'Clausena lenis', 'Cleistochlamys kirkii', 'Clematis ganpiniana', 'Cleome droserifolia', 'Clerodendrum kiangsiense', 'Clerodendrum viscosum', 'Clinacanthus nutans', 'Clinacanthus nutansindau', 'Clusia rosea', 'Cnidium monnieri', 'Cnidium officinale', 'Coffea arabica', 'Coleus hybridus', 'Colocasia esculenta', 'Commiphora africana', 'Commiphora mukul', 'Commiphora opobalsamum', 'Coprinus comatus', 'Coptidis rhizoma', 'Coptis chinensis', 'Cordyceps bassiana', 'Cordyceps militaris', 'Cordyceps sinensis', 'Coriandrum sativum', 'Coriolus versicolor', 'Cornus mas', 'Corydali syanhusuo', 'Corydalis govaniana', 'Corydalis saxicola', 'Corydalis turtschaninovii', 'Corydalis yanhusuo', 'Corydalis yanhusuo W. T. Wang', 'Corylus avellana', 'Costus speciosus', 'Cotinus coggygria Scop.', 'Cotton plant (Gossypium species), Thespesia populnea', 'Cranberry', 'Crataegus gracilior', 'Crataegus pinnatifida', 'Cratoxy formosum', 'Cratoxylum cochinchinense', 'Crinum amabile', 'Crocus sativus', 'Croton crassifolius', 'Croton gratissimus', 'Croton kongensis', 'Croton oblongifolius', 'Croton oblongus', 'Cruciferous vegetables', 'Cruciferous vegetables (Brassica oleracea)', 'Cryptocarya latifolia', 'Cryptocarya yunnanensis', 'Cucumis melo', 'Cudrania tricuspidata', 'Culture filtrate of endophytic Streptomyces sp. YIM66017 from Alpinia oxyphylla', 'Cunila lythrifolia', 'Cuphea aequipetala', 'Cupressus sempervirens', 'Curcuma longa', 'Curcuma wenyujin', 'Curcuma xanthorrhiza', 'Curcuma zedoaria', 'Curcumin - Curcuma longa  Berberine - Thalictrum delavayi', 'Cuscuta chinensis', 'Cyathostemma argenteum', 'Cyclopia genistoides', 'Cyclopia subternata', 'Cymbopogon nervatus', 'Cymbopogon schoenanthus', 'Cynanchum auriculatum', 'Cynanchum paniculatum', 'Cynanchum wilfordii', 'Cynara cardunculus', 'Cynara scolymus', 'Cyperus longus', 'Cyperus rotundus', 'Cystoseira barbata', 'Cystoseira crinita', 'Dalbergia velutina', 'Daphne genkwa', 'Daphne genkwa, Daphne mezereum', 'Daphne gnidium', 'Datura stramonium (DS) and Datura inoxia (DI)', 'Daucus carota', 'Daucus carrota', 'Decalepis hamiltonii', 'Dendrobium nobile', 'Dendrophthoe pentandra', 'Descurainia sophia', 'Dichroa febrifuga', 'Dicranopteris linearis', 'Dictamnus dasycarpus', 'Dillenia suffruticosa', 'Dioscorea bulbifera', 'Dioscorea collettii', 'Dioscorea membranacea', 'Dioscorea villosa', 'Diospyros lotus', 'Diospyros lycioides', 'Diospyros shimbaensis', 'Diospyros undulata', 'Dittrichia viscosa', 'Dracocephalum kotschyi', 'Dracocephalum surmandinum', 'Dryobalanops rappa', 'Dryopteris fragrans', 'Dunaliella tertiolecta', 'Dysoxylum binectariferum', 'Echinophora Platyloba', 'Eclipta alba', 'Elaeis guineensis', 'Elaeocarpus petiolatus', 'Elaeodendron orientale', 'Elephantopus mollis Kunth', 'Elephantopus scaber', 'Eleutherococcus senticosus', 'Eleutherococcus trifoliatus', 'Ellipeiopsis cherrevensis', 'Embelia ribes', 'Emblica officinalis', 'Endophytic Chaetomium sp 88194', 'Endophytic fungus Aspergillus nidulans, associated with Nyctanthes arbor-tristisinn.', 'Endophytic fungus Mycoleptodiscus sp', 'Endophytic fungus Phoma species ZJWCF006 in Arisaema erubescens', 'Endophytic fungus of Xylocarpus granat', 'Endophytic fungus of Xylocarpus granatum', 'Engleromyces goetzii', 'Ephedra sinica', 'Epimedium brevicornum', 'Epimedium diphyllum', 'Epipremnum pinnatum (L)', 'Erigeron breviscapus', 'Eriobotrya japonica', 'Eruca sativa', 'Erycibe elliptilimba', 'Erythrina abyssinica', 'Erythrina corallodendron', 'Erythrina excelsa', 'Erythrina orientalis', 'Erythronium japonicum', 'Ethyl acetate (EtOAc) extracts of Phoma sp. JS0228 cultures, an endophytic fungus of Morus alba (M. alba)', 'Eucalyptus robusta', 'Euclea crispa', 'Eugenia aquea', 'Eugenia jambolana', 'Eugenia pyriformis', 'Eupatorium album', 'Eupatorium fortunei', 'Eupatorium lindleyanum', 'Euphorbia bicolor', 'Euphorbia ebracteolata', 'Euphorbia fischeriana', 'Euphorbia hirta', 'Euphorbia humifusa', 'Euphorbia jolkini', 'Euphorbia kopetdaghi', 'Euphorbia lathyris', 'Euphorbia microsciadia', 'Euphorbia pubescens', 'Euphorbia sororia', 'Euphorbia supina', 'Euphorbia szovitsii Fisch & CAMey', 'Euphorbia tirucalli', 'Eurycoma longifolia', 'Eurycoma longifolia Jack', 'Euscaphis japonica', 'Euterpe oleracea', 'Evodia rutaecarpa', 'Evolvulus alsinoides', 'Fagonia indica', 'Fallopia convolvulus', 'Ferula assa-foetida', 'Ferula ferulaeoides', 'Ferula gummosa', 'Ferula hermonis', 'Ferula oopoda', 'Ferula ovina', 'Ferula persica', 'Ferula szowitsiana', 'Ferulago angulata', 'Ferulago carduchorum', 'Ficus altissima', 'Ficus carica', 'Ficus crocata', 'Ficus fistulosa', 'Ficus hispidaf', 'Ficus salicifolia', 'Ficus septica', 'Fissistigma oldhamii', 'Flacourtia rukam Zoll & Moritzi', 'Foeniculum vulgare', 'Forsythia koreana', 'Forsythia suspensa', 'Fragaria ananassa', 'Frangula alnus', 'Fraxinus bungeana', 'Fritillaria hupehensis', 'Fusarium oxysporum EPH2RAA endophytic in Ephedra fasciculata', 'Gaillardia pulchella', 'Galium aparine', 'Ganoderma lucidum', 'Ganoderma lucidum and Polyporus umbellatus', 'Ganoderma sinense', 'Garcinia atroviridis', 'Garcinia bracteata', 'Garcinia celebica', 'Garcinia epunctata', 'Garcinia hanburyi', 'Garcinia hombroniana', 'Garcinia indica', 'Garcinia mangostana', 'Garcinia nervosa', 'Garcinia penangiana', 'Garcinia quaesita', 'Garcinia tetrandra', 'Garcinia wightii', 'Geissospermum sericeum', 'Genista tinctoria', 'Ginkgo biloba', 'Glandora rosmarinifolia', 'Glaucium flavum', 'Gleditsia sinensis', 'Glehnia littoralis', 'Glossogyne tenuifolia', 'Glycine max', 'Glycyrrhiza glabra', 'Glycyrrhiza glabra(licorine)', 'Glycyrrhiza inflata', 'Glycyrrhiza uralensis', 'Goniothalamus cheliensis', 'Goniothalamus elegants Ast', 'Goniothalamus laoticus', 'Goniothalamus macrocalyx Ban', 'Goniothalamus tamirensis', 'Gossypium herbaceum', 'Grammatophyllum speciosum', 'Grifola frondosa', 'Guaiacum sanctum and Guaiacum officinale', 'Gynostemma pentaphyllum', 'Halophila ovalis', 'Hancornia speciosa', 'Handroanthus impetiginosus', 'Haplopappus rigidus phil.', 'Hedychium spicatum', 'Hedyotis diffusa', 'Helianthus genus', 'Helicteres isora', 'Helminthostachys zeylanica', 'Hemerocallis fulva', 'Hemsleya delavayi', 'Hibiscus Syriacus', 'Hibiscus rosa-sinesis', 'Hibiscus syriacus', 'Horsfieldia superba', 'Houttuynia cordata', 'Humboldtia unijuga', 'Humulus lupulus', 'Humulus lupulus (Common hop)', 'Hyacinthus orientalis', 'Hydnophytum formicarum', 'Hygrophorus eburneus', 'Hypecoum leptocarpum', 'Hypericum elodeoides', 'Hypericum perforatum', 'Hypericum salsugineum', 'Hypericum undulatum', 'Icacina trichantha', 'Impatiens balsamina', 'Imperata cylindrica', 'Indigofera tinctoria', 'Inula aucheriana', 'Inula britannica', 'Inula lineariifolia Turcz', 'Inula viscosa', 'Ipomoea batatas', 'Iris Nertschinskia', 'Iris lactea', 'Isodon adenolomus', 'Isodon eriocalyx', 'Isodon forrestii var forrestii', 'Isodon japonica Hara var glaucocalyx', 'Isodon lophanthoides', 'Isodon rubescens', 'Jatropha curcas', 'Jatropha gossypifolia', 'Jatropha gossypiifolia', 'Juglans mandshurica', 'Juglans regia', 'Juncus effusus', 'Juniperus communis', 'Juniperus communis.', 'Juniperus polycarpos', 'Justicia gendarussa', 'Kadsura heteroclita () Craib (Schizandraceae)', 'Kelussia odoratissima', 'Kigelia Africana, Ximenia Caffra and Mimusops Zeyheri', 'Kochia scoparia Scharder', 'Kokoona zeylanica', 'Kola acuminate', 'Kopsia fruticosa', 'Korean red ginseng', 'Labisia pumila', 'Lagerstroemia speciosa', 'Lampranthus aurantiacus', 'Lampranthus glaucus', 'Lantana camara', 'Larrea divaricata', 'Larrea tridentata', 'Laurencia viridis sp nov', 'Laurenciaintricata', 'Lavandula angustifolia', 'Lavandula coronopifolia', 'Lawsonia inermis', 'Lentinula edodes(mushroom)', 'Lentinus edodes', 'Leonurus cardiaca', 'Leonurus japonicus', 'Lepidium sativum', 'Leptadenia pyrotechnica', 'Lespedeza cuneata', 'Leucobryum bowringii Mitt', 'Licania rigida', 'Licania tomentosa', 'Lignosus rhinocerotis', 'Ligularia fischeri', 'Ligularia songarica', 'Limoniastrum guyonianum', 'Lindera', 'Lindera erythrocarpa', 'Lindera umbellata', 'Linum usitatissimum', 'Linum usitatissimum (Flaxseed)', 'Linum usitatissium', 'Lippia citriodora', 'Lippia origanoides', 'Liriope muscari', 'Liriope platyphylla', 'Lithospermum erythrorhizon', 'Livistona chinensis', 'Lobelia inflata', 'Lonicera japonica', 'Lonicera similis Hemsl', 'Lotus ucrainicus', 'Luehea candicans', 'Lycium barbarum', 'Lyonia ovalifolia', 'Lyonia ovalifolia var hebecarpa', 'Macaranga tanarins', 'Machilus thunbergii', 'Macleaya cordata', 'Maclura cochinchinensis', 'Maclura pomifera', 'Macrothelypteris torresiana', 'Maesa macrophylla', 'Magnolia obovata', 'Magnolia officinalis', 'Mallotus philippinensis', 'Malus domestica', "Malus domestica 'Cripps Pink'", 'Malus niedzwetzkyana', 'Malus pumila', 'Malus pumila Miller cv Annurca', 'Mammea americana', 'Mangifera indica', 'Mangifera pajang', 'Mangifera zeylanica', 'Manilkara zapota.', 'Mansonia gagei', 'Mappianthus iodoies', 'Mappianthus iodoies, Cornus kousa, Eria bambusifolia', 'Marila pluricostata', 'Marrubium crassidens', 'Marrubium persicum', 'Matricaria chamomilla', 'Maytenus cuzcoina, Maytenus canariensis, Maytenus magellanica, Maytenus chubutensis', 'Maytenus disticha', 'Melaleuca Alternifolia', 'Melia azedarach', 'Melia azedarach.', 'Melilotus officinalis', 'Melissa officinalis', 'Melissa officinalis, Rosemary plant \n Salvia officinalis', 'Melodinus fusiformis', 'Mentha arvensis', 'Meriandra dianthera', 'Mexican poleo', 'Millettia ferruginea', 'Millettia versicolor', 'Mimusops zeyheri', 'Miquelia dentata', 'Mitragyna diversifolia', 'Momordica charantia', 'Momordica cochinchinensis', 'Monosporascus eutypoides', 'Montanoa guatemalensis', 'Morinda citrifolia', 'Morinda citrifoliainn', 'Moringa oleifera', 'Moringa stenopetala', 'Morus alba', 'Morus nigra', 'Morus nigra.', 'Mundulea sericea', 'Murraya euchrestifolia', 'Murraya koenigii', 'Murraya paniculata', 'Muscadinia rotundifolia', 'Mushroom Tricholoma pardinum', 'Myoporum bontioides (endophytic fungus Trichoderma sp. 09)', 'Myrica rubra', 'Myristica argentea', 'Myrtus communis', 'Nasturtium officinale', 'Nauclea orientalis', 'Nelumbo nucifera', 'Neosartorya glabra', 'Nepeta menthoides', 'Newbouldia laevis', 'Niebla homalea', 'Nigella sativa', 'Nothapodytes foetida', 'Nothapodytes nimmoniana', 'Nymphaea alba', 'Ochradenus arabicus', 'Ocimum basilicum', 'Ocimum gratissimum', 'Ocimum tenuiflorum', 'Oldenlandia diffusa', 'Olea Europea', 'Olea europaea', 'Oliveria decumbens', 'Onobrychis ebenoides', 'Onopordum acanthium', 'Onosma hookeri', 'Ophiopogon japonicus', 'Oplopanax horridus', 'Orbignya speciosa', 'Origanum acutidens', 'Origanum compactum', 'Origanum majorana', 'Origanum munzurense', 'Orobanche amethystea', 'Orobanche crenata', 'Oroxylum indicum', 'Oryza sativa', 'Pachypodium lamerei Drake', 'Pachysandra terminalis', 'Paecilomyces tenuipes', 'Paeonia lactiflora', 'Paeonia suffruticosa', 'Pallenis spinosa', 'Palm oil and Grapefruit respectively', 'Palm oil and Oranges respectively', 'Palm oil and Soybean respectively', 'Palm oil and Tangerine respectively', 'Palm oil and various plants respectively', 'Palm oil/Palm fruits', 'Panax ginseng', 'Panax notoginseng', 'Pancratium maritimum', 'Pandanus amaryllifolius', 'Papaver rhoeas', 'Papaver somniferum', 'Paraconiothyrium hawaiiense', 'Paramignya trimera', 'Parinari curatellifolia', 'Paris polyohylla', 'Paris polyohylla var chinensis', 'Paris polyphylla', 'Paris polyphylla Sm', 'Paris quadrifolia', 'Parkinsonia aculeata', 'Parmotrema reticulatum', 'Passiflora incarnata', 'Patrinia scabiosaefolia', 'Patrinia villosa', 'Pavetta indica', 'Peach and Plum', 'Peganum harmala', 'Peganum nigellastrum', 'Pelingo apple', 'Penicillium griseum', 'Penicillium sp', 'Pergularia tomentosa', 'Perilla frutescens', 'Periploca hydaspidis', 'Perovskia abrotanoides', 'Persea americana', 'Persicaria maculosa', 'Peucedanum japonicum', 'Pfaffia paniculata', 'Phaleria macrocarpa', 'Phaleria macrocarpa (Scheff) Boerl', 'Pharbitis nil', 'Phaseolus angularis', 'Phaseolus vulgaris', 'Phellodendron amurense', 'Phlogacanthus thyrsiformis', 'Phlomis russeliana', 'Phlomis viscosa Poiret', 'Phoenix Dan Cong tea', 'Phoenix dactylifera', 'Phyllanthus amarus', 'Phyllanthus amarus Schum & Thon', 'Phyllanthus emblica', 'Phyllanthus niruri', 'Phyllanthus urinariainn\nNephelium lappaceum', 'Phyllostachys heterocycla', 'Phyllostachys heterocycla var. pubescens', 'Physalis angulate.', 'Physalis minima', 'Phytolacca acinosa', 'Picramnia glazioviana Engl.', 'Picrasma quassioides', 'Picrorhiza kurroa', 'Pinus koraiensis', 'Pinus nigra', 'Piper longum', 'Piper methsyticum', 'Piper nigrum', 'Piper nigrum \n Piper longum', 'Piper sarmentosum', 'Pistacia atlantica', 'Pistacia integerrima', 'Pisum sativum', 'Pithecellobium dulce', 'Plant endophytic fungi Phomosis sp', 'Plantago major', 'Plantago media', 'Platycodon grandiflorus', 'Plectranthus amboinicus', 'Pleiocarpa pycnantha', 'Plenckia populnea', 'Pleurotus ostreatus (oyster mushroom)', 'Plinia cauliflora', 'Pluchea dioscoridis', 'Plumbago zeylanica', 'Podocarpus nagi', 'Podocytisus caramanicus', 'Podophyllum hexandrum', 'Pogostemon quadrifolius (Benth.)', 'Polygonatum odoratum', 'Polygonum amplexicaule D. Don var. sinense Forb', 'Polygonum avicular', 'Polygonum cognatum', 'Polygonum cuspidatum', 'Polygonum hydropiper', 'Polygonum multiflorum Thunb.', 'Poncirus trifoliata', 'Populus tremula (poplar)', 'Poria cocos', 'Porphyridium cruentum', 'Potentilla fulgens', 'Pothos scandens', 'Pouteria torta', 'Premna odorata', 'Premna tomentosa', 'Prinsepia utilis', 'Prinsepia utilis Royle', 'Propolis, Euonymus alatus (Winged Spindle Tree)', 'Prosopis juliflora', 'Prunella vulgaris', 'Prunus amygdalus Batsch', 'Prunus avium', 'Prunus dulcis', 'Prunus persica', 'Prunus salicina', 'Prunus spinosa', 'Pseuderanthemum palatiferum', 'Pseudevernia furfuracea', 'Pseudolarix kaempferi', 'Pseuduvaria monticola', 'Pseuduvaria trimera', 'Psidium guajava', 'Psidium guajava \nCudranaia tricuspidata', 'Psidium guajava (Guava)', 'Psidium guajava, Origanum vulgare, Cinnamomum spp, Eugenia caryophyllata, Piper nigrum', 'Psilostrophe cooperi', 'Psoralea corylifolia', 'Psychotria klugii', 'Pteris Quadriureta', 'Pterogyne nitens', 'Pterospermum yunnanense', 'Pueraria lobata', 'Pulicaria undulata', 'Pulsatilla chinensis', 'Pulveroboletus ravenelii', 'Punica granatum', 'Putranjiva roxburghii', 'Putterlickia pyracantha', 'Puya laxa', 'Pyracantha fortuneana', 'Pyrenacantha staudtii', 'QDG is composed of eleven herbs, such as Bupleuri Radix (Bupleurum chinense DC, root), Citri Reticulatae Pericarpium (Citrus reticulata Blanco, peel), Curcumae Radix (Curcuma wenyujin Y H Chen et Cing, root tuber), Sophorae Flos (Sophora japonica, flower), Moutan Cortex (Paeonia suffruticosa Andr, root bark), Arnebiae Radix (Arnebia euchroma (Royle) Johnst, root), Prunellae Spica (Prunella vulgaris, ear), Salviae Miltiorrhizae Radix et Rhizoma (Salvia miltiorrhiza Bge, root and rhizome), Curcumae Rhizoma (Curcuma phaeocaulis Val, root tuber), Astragali Radix (Astragalus membranaceus (Fisch) Bge var mongholicus (Bge) Hsiao, root), and Glycyrrhizae Radix et Rhizoma (Glycyrrhiza uralensis Fisch, root and rhizome)', 'Quercus acutissima', 'Quercus aliena', 'Quercus infectoria', 'Quercus macrocarpa', 'Quercus robur', 'Rabdosia rubescens', 'Radix Bupleuri', 'Radix Salviae Miltiorrhizae', 'Radix astragali', 'Radix et Rhizomaeonticis', 'Radix stephaniae tetrandrae', 'Ranunculus ternatus Thunb', 'Reissantia buchananii', 'Retama sphaerocarpa', 'Rhazya stricta', 'Rheum emodi', 'Rheum palmatum', 'Rheum tanguticum Maxim ex Balf (rhubarb)', 'Rheum undulatum', 'Rhinacanthus nasutus', 'Rhizoma drynariae', 'Rhizophora apiculata', 'Rhizopus chinensis', 'Rhodiola crenulata', 'Rhodiola rosea', 'Rhus verniciflua', 'Rosmarinus officinalis', 'Rothmannia wittii', 'Rubia cordifolia', 'Rubia tinctorum', 'Rubus coreanus', 'Rubus crategifolius', 'Rubus fairholmianus', 'Rubus fruticosus', 'Rubus idaeus', 'Rubus occidentalis', 'Rumex crispus.', 'Rumex dentatus', 'Rumex nervosus', 'Rumex vesicarius', 'Russula delica', 'Saccharomyces cerevisiae', 'Salacia oblonga', 'Salicornia bigelovii', 'Salicornia herbacea', 'Salix safsaf', 'Salvia africana', 'Salvia atropatana', 'Salvia buchananii', 'Salvia corrugata', 'Salvia deserta', 'Salvia digitaloides', 'Salvia dominica', 'Salvia fruticosa', 'Salvia hormium', 'Salvia miltiorrhiza', 'Salvia miltiorrhizae Binge', 'Salvia reuterana', 'Salvia sclarea', 'Salvia syriaca', 'Salvia tebesana Bunge', 'Salvia tomentosa', 'Sanguinaria canadensis', 'Sanguisorba officinalis', 'Santalum album', 'Santolina corsica Jord', 'Saposhnikovia divaricata', 'Sarcococca hookeriana', 'Sargassum angustifolium', 'Sargassum boveanum', 'Sargassum linearifolium', 'Sargassum oligocystum', 'Sasa borealis', 'Satureja khuzestanica', 'Satureja khuzestanica Jamzad', 'Satureja spicigera', 'Sauromatum giganteum', 'Saururus cernuus', 'Saururus chinensis', 'Saussurea lappa', 'Saussurea phyllocephala', 'Schima wallichii', 'Schinus molle', 'Schisandra chinensis', 'Schisandra chinesis', 'Schisandra viridis', 'Schisandrae Chinensis', 'Schizophyllum commune', 'Schumacheria castaneifolia', 'Scrophularia atropatana', 'Scrophularia frigida Boiss', 'Scrophularia oxysepala', 'Scrophularia umbrosa Dumort', 'Scutellaria baicalensis', 'Scutellaria barbata', 'Scutellaria litwinowii', 'Scutellaria strigillosa', 'Scutelleria baicalensis', 'Selaginella repanda', 'Selaginella trichoclada', 'Semecarpus anacardium', 'Semialarium mexicanum', 'Senecio glaucus.', 'Senecio rhizomatus Rusby', 'Serenoa repens', 'Sesamum indicum', 'Sesamum indicum, \nZanthoxylum capense, \nZanthoxylum paracanthum Kokwaro,\n Peperomia pellucida, \nZanthoxylum nitidum, \nHomalomena wendlandii, \nStemona pierrei,\nKnema glauca, \nTriclisia sacleuxii, \nZanthoxylum setulosum', 'Shiraia bambusicola', 'Sideritis leucantha', 'Siegesbeckia orientalis', 'Silphium radula Nutt', 'Silybum marianum', 'Simarouba tulae', 'Sinomenium acutum', 'Sinopodophyllum hexandrum', 'Smilax china', 'Smilax spinosa Miller', 'Solanum chacoense', 'Solanum lycopersicum', 'Solanum lyratum', 'Solanum nigrum', 'Solanum torvum', 'Sophora alopecuroides', 'Sophora flavescens', 'Sophora interrupta', 'Sophora tonkinensis', 'Sour jujube', 'Soymida febrifuga', 'Sparganii Rhizoma', 'Spatholobus suberectus', 'Sphagneticola calendulacea', 'Sphagneticola trilobata', 'Spinacia oleracea', 'Spiranthes australis', 'Spondias pinnata', 'Stachys byzantina C. Koch', 'Stachys persica S.G.Gmel. ex C.A.Mey', 'Stachys pilifera Benth.', 'Staphisagria macrosperma', 'Stellera chamaejasme', 'Stemona pierrei', 'Stemona tuberosa', 'Stephania delavayi', 'Stephania epigaea', 'Stephania japonica', 'Stereocaulon alpinum', 'Sternbergia clusiana', 'Stevia rebaudiana', 'Strobilanthes crispa', 'Strobilanthes crispus', 'Strophanthus kombe', 'Strophioblachia fimbricalyx', 'Strychnos nux-vomica', 'Strychnos nux-vomica.', 'Styrax perkinsiae\n Gastrodia elata Blume\n Zanthoxylum nitidum\n Goniothalamus laoticus', 'Sutherlandia frutescens', 'Swertia chirata', 'Syzygium aromaticum', 'Tabebuia avellandae', 'Tabernaemontana catharinensis', 'Tabernaemontana corymbosa', 'Tabernaemontana divaricata, Tabernaemontana corymbosa', 'Tagetes minuta', 'Taiwania cryptomerioides', 'Taiwanofungus camphoratus', 'Tamarix aphylla', 'Tamarix articulata', 'Tanacetum parthenium', 'Tanacetum polycephalum', 'Tanshinone IIA - Salvia miltiorrhiza Andrographolide - Andrographis paniculata', 'Taraxacum mongolicum', 'Taxus baccata', 'Taxus brevifolia', 'Taxus chinensis', 'Taxus cuspidata', 'Taxus yunnanensis', 'Tecoma stans', 'Tephroseris kirilowii', 'Tephrosia candida, Pongamia pinnata,onchocarpus costaricensis', 'Tephrosia uniflora', 'Terminalia arjuna', 'Terminalia belerica', 'Terminalia bellirica', 'Terminalia chebula', 'Terminalia citrina', 'Tetradenia riparia', 'Tetrastigma hemsleyanum', 'Tetrastigma hemsleyanum\nHoney', 'Teucrium polium', 'Thalassodendron ciliatum', 'Thalictrum foliolosum', 'Thymbra Spicata', 'Thymelaea hirsuta', 'Thymus caramanicus Jalas', 'Thymus vulgaris', 'Tillandsia recurvata', 'Tinospora cordifolia', 'Toona ciliata\n Chisocheton siamensis', 'Toona ciliata var yunnanensis', 'Toona ciliata, Neem', 'Toona ciliata, Trichilia catigua', 'Torilis japonica', 'Trachycarpus fortunei', 'Trachyspermum anethifolium', 'Tragopogon orientalis', 'Tragopogon porrifolius (Salsify)', 'Trametes robiniophila murr', 'Trametes versicolor', 'Trapa acornis', 'Trichosanthes cucumerina', 'Trichosanthes kirilowli', 'Triclisia sacleuxii', 'Trifolium pratense', 'Trigonella berythea', 'Trigonella foenum-graecum', 'Trigonella foenum-graecum\n Paris polyphylla', 'Trigonostemon howii', 'Trillium tschonoskii', 'Tripterygium regelii', 'Tripterygium wilfordii', 'Tripterygium wilfordii Hook F', 'Triticum aestivum', 'Trollius chinensis', 'Turraea nilotica', 'Turraea nilotica\nTurraea robusta', 'Turraea robusta', 'Tussilago farfara', 'Tylophora indica', 'Typhonium flagelliforme', 'Uncaria rhynchophylla', 'Uncaria tomentosa', 'Undaria pinnatifida', 'Urtica dioica', 'Usnea strigosa', 'Vaccinium corymbosum', 'Vaccinium macrocarpon', 'Vaccinium myrtillus (Bilberry )', 'Valeriana jatamansi Jones', 'Valeriana officinalis', 'Vernonia amygdalina', 'Vernonia anthelmintica', 'Vernonia anthelmintica, \nVernonia extensa, \nCentratherum anthelminticum (L)', 'Vernonia anthelmintica, \nVernonia guineensis Benth (Asteraceae)', 'Vernonia divaricata', 'Vernonia zeylanica', 'Veronica peregrina', 'Verticillium dahliae', 'Viburnum odoratissimum', 'Vicia monantha', 'Viscum album', 'Viscum coloratum', 'Vismia laurentii', 'Vitex agnus-castus', 'Vitex rotundifolia', 'Vitis coignetiae Pulliat', 'Vitis palmata', 'Vitis rotundifolia', 'Vitis rupestris', 'Vitis thunbergii', 'Vitis vinifera', 'Voacanga africana', 'Wedelia biflora', 'Wikstroemia scytophylla', 'Withania coagulans', 'Withania somnifera', 'Wollastonia biflora', 'Xanthium strumarium', 'Ximenia caffra', 'Xylopia aromatica', 'Xylopia sericea', 'Yucca aloifolia variegata', 'Zanthoxylum nitidum', 'Zanthoxylum piperitum', 'Zanthoxylum setulosum', 'Zanthoxylum zanthoxyloides', 'Zea mays', 'Zhumeria majdae', 'Zingiber cassumunar', 'Zingiber officinale', 'Zingiber officinale (Ginger)', 'Zingiber zerumbet', 'Ziyang green tea', 'Ziziphus jujube', 'Ziziphus lotus', 'Ziziphus spina-christi', 'Zizyphus jujuba']
        plnt =re.compile('|'.join(pl_list))
        if pat.match(Phytochemical):
            print (Phytochemical)
            catagory =Phytochemical
            cur=db.execute('select  * from phyto_chemicals where Type_of_phytochemicalsextract  Like ?', [catagory])
            results=cur.fetchall()
            print (cur)
            df1=pd.DataFrame(results)
            print(df1)
            if not results:
                flash ('Something went wrong!','error')
                flash ('There is not Phytochemical with this letter in the database !!','info')
                return redirect(url_for('index'))
            else:
        	    df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
        	    df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           
        	    selectdf=df[[ "PhytoCAT-ID" ,"Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  

            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
        	    Feature=  "Phytochemicals Category : "+ catagory
        	    selectdf = selectdf.fillna(value='NA')

        	    selectdf.columns=[  "PhytoCAT-ID" ,"Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  
  

        	    return render_template('plants_results.html',Feature= Feature, selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )

        elif plnt.match(Phytochemical):
            Plant =Phytochemical
            cur=db.execute('select  * from phyto_chemicals where Source_of_phytochemicals_Name_of_Plant=?',[Plant])

            #cur=db.execute('select  * from phyto_chemicals where Type_of_phytochemicalsextract  Like ?', [catagory])
            results=cur.fetchall()
            print (cur)
            df1=pd.DataFrame(results)
            print(df1)
            if not results:
                flash ('Something went wrong!','error')
                flash ('There is not Phytochemical with this letter in the database !!','info')
                return redirect(url_for('index'))
            else:
        	    df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
        	    df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           
        	    selectdf=df[[ "PhytoCAT-ID" ,"Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  

            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
        	    Feature= "Plant name : "+ Plant

        	    selectdf = selectdf.fillna(value='NA')

        	    selectdf.columns=[  "PhytoCAT-ID" ,"Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  
  

        	    return render_template('plants_results.html',Feature= Feature, selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )


                
        else :
            cur=db.execute('select  * from phyto_chemicals where Phytochemicalextract_name=?',[Phytochemical])
            results=cur.fetchall()
            print (results)
            df1=pd.DataFrame(results)
            print(df1)
            if not results:
        	    flash ('Something went wrong!','error')
        	    flash ('The entered Phytochemical name is not valid !!','info')

        	    return redirect(url_for('index'))
            else:
                df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" , "Phytochemical name or plant extracts" , "PMID" , "Literature evidence" , "IUPAC name" , "Phytochemicals’ class or type of plant extracts" , "Source of phytochemicals or plant Extracts","Geographical availability","Plant parts","Other cancers","Target gene or protein","Gene or Protein evidence","Target pathways","IC50","Potency","Study type","Additional information ","PubChem ID","Additional PMIDs","Additional sources of information","Safety"])
                df['Source of phytochemicals or plant Extracts']=df['Source of phytochemicals or plant Extracts'].str.replace(r"\(.*\)","")
                df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)
                df['PMID']=df['PMID'].astype(float).astype(int)
                if df['PubChem ID'][0] != None:
                    df['PubChem ID']=df['PubChem ID'].str.replace('NCT*.*','')
                    df['PubChem ID']=df['PubChem ID'].str.replace(', *.*','')
                    df['PubChem ID']=df['PubChem ID'].astype(float).astype(int)
                df1=df.transpose().reset_index()
                if len(df1.columns) == 3 :
                    df1.columns=['Properties','Information1','Information2']
                    df1 = df1.fillna(value='NA')
                else :
                    df1.columns=['Properties','Information']
                    df1 = df1.fillna(value='NA')
                if form.validate_on_submit():
                    if len(df1.columns) == 3   :
                        return render_template('jatayu2_results_multi.html',Phytochemical=Phytochemical,df1=df1, tables=[df1.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )
                    else :
                        return render_template('jatayu2_results.html',Phytochemical=Phytochemical,df1=df1, tables=[df1.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )



    
                

   # return render_template('index.html',form=form)#,visitors=counter)

    return render_template('front1.html',form=form)


@app.route('/contact')
def contact1():
    return render_template('contact.html')

@app.route('/help')
def help1():
    return render_template('help.html')

@app.route('/faq')
def faq1():
    return render_template('faqs.html')


@app.route('/chemical', methods=['GET', 'POST'])
def form():
    #global counter
    #counter += 1
    db=get_db()
    form = MyForm()
    #form = MyForm()
    if request.method == 'POST' :
        #rsid1=request.form['RSID']
        Phytochemical=form.Phytochemical.data
        #return render_template()
        #return '<h1>RSID:{}'.format(rsid1)
        print(Phytochemical)
        #POS=81737298

        cur=db.execute('select  * from phyto_chemicals where Phytochemicalextract_name=?',[Phytochemical])
        #cur=db.execute('select  * from jatayu_dbsnps_updated_full where RS=?',[rsid1])

        results=cur.fetchall()
        print (results)
        df1=pd.DataFrame(results)
        print(df1)
        
        if not results:
            flash ('Something went wrong!','error')
            flash ('The entered Phytochemical name is not valid !!','info')

            return redirect(url_for('form'))
            
        else:
            #df = pd.DataFrame(results, columns =[ "S. No." ,"Phytochemical_nameextract" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" , "Phytochemical name or plant extracts" , "PMID" , "Literature evidence" , "IUPAC name" , "Phytochemicals’ class or type of plant extracts" , "Source of phytochemicals or plant Extracts","Geographical availability","Plant parts","Other cancers","Target gene or protein","Gene or Protein evidence","Target pathways","IC50","Potency","Study type","Additional information ","PubChem ID","Additional PMIDs","Additional sources of information","Safety"]) 
            df['Source of phytochemicals or plant Extracts']=df['Source of phytochemicals or plant Extracts'].str.replace(r"\(.*\)","")
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)                
            df['PMID']=df['PMID'].astype(float).astype(int)
            if df['PubChem ID'][0] != None:            
             df['PubChem ID']=df['PubChem ID'].str.replace('NCT*.*','')
             df['PubChem ID']=df['PubChem ID'].str.replace(', *.*','')

             df['PubChem ID']=df['PubChem ID'].astype(float).astype(int)

            df.to_csv("test_datasets.csv",index=False)
            df1=df.transpose().reset_index()
            if len(df1.columns) == 3 :
             df1.columns=['Properties','Information1','Information2']
             #df1.drop(index=df1.index[:1], axis=0, inplace=True)
             df1 = df1.fillna(value='NA')

            else :
             df1.columns=['Properties','Information']
             #df1.drop(index=df1.index[:1], axis=0, inplace=True)
             df1 = df1.fillna(value='NA')





            #df1=df1.drop([0,2])
            print (df1)
            

            if form.validate_on_submit():
             if len(df1.columns) == 3   :
              return render_template('jatayu2_results_multi.html',Phytochemical=Phytochemical,df1=df1, tables=[df1.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )
             else :
              return render_template('jatayu2_results.html',Phytochemical=Phytochemical,df1=df1, tables=[df1.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )



    
                

    return render_template('index.html',form=form)#,visitors=counter)

@app.route('/plant', methods=['GET', 'POST'])
def form1():
    #global counter
    #counter += 1
    db=get_db()
    form = Plants()
    #form = MyForm()
    if request.method == 'POST' :
        #rsid1=request.form['RSID']
        Plant=form.Plant.data
        #return render_template()
        #return '<h1>RSID:{}'.format(rsid1)
        print(Plant)
        #POS=81737298

        cur=db.execute('select  * from phyto_chemicals where Source_of_phytochemicals_Name_of_Plant=?',[Plant])
        #cur=db.execute('select  * from jatayu_dbsnps_updated_full where RS=?',[rsid1])

        results=cur.fetchall()
        print (results)
        #df1=pd.DataFrame(results)
        #print(df1)
        
        if not results:
            flash ('Something went wrong!','error')
            flash ('The entered Plant name is not valid !!','info')

            return redirect(url_for('form1'))
            
        else:
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df.to_csv("test_datasets.csv",index=False)
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)
            selectdf=df[[  "PhytoCAT-ID" ,"Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  
            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
            Feature= "Plant name : "+ Plant
            selectdf = selectdf.fillna(value='NA')

            selectdf.columns=["PhytoCAT-ID","Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  


            if form.validate_on_submit():
             return render_template('plants_results.html',Feature=Feature,selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )


    
                

    return render_template('plant.html',form=form)#,visitors=counter)

@app.route('/gene', methods=['GET', 'POST'])
def form2():

    gene_ls=pd.read_csv("/home/igib/Phytocat/phytocatdb/db/Phytochemical_genes.tsv",sep="\t")
    return render_template('gene_results.html',selectdf=gene_ls, tables=[gene_ls.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )


    
                

    return render_template('gene.html',form=form)#,visitors=counter)    


@app.route("/pmid", methods=['GET', 'POST'])
def pmid():
    ids = request.args.get('ids', None)

    ids=str(ids)
    db=get_db()
    #alphabetname=ids
    #alphabet=ids+'%'
    print(ids)

    #cur=db.execute('select  * from phyto_chemicals where ?  Like ?',('Phytochemical_nameextract', alphabet))
    cur=db.execute('select  * from phyto_chemicals where PMID   =?', [ids])   #=?',[Phytochemical]

    results=cur.fetchall()
    #print (results)
    df1=pd.DataFrame(results)
    print(df1)

    if not results:
            flash ('Something went wrong!','error')
            flash ('There is not Phytochemical with this letter in the database !!','info')

            return redirect(url_for('pmid'))
            
    else:
            df = pd.DataFrame(results, columns =[ "S. No." , "Phytochemical name or plant extracts" , "PMID" , "Literature evidence" , "IUPAC name" , "Phytochemicals’ class or type of plant extracts" , "Source of phytochemicals or plant Extracts","Geographical availability","Plant parts","Other cancers","Target gene or protein","Gene or Protein evidence","Target pathways","IC50","Potency","Study type","Additional information ","PubChem ID","Additional PMIDs","Additional sources of information","Safety"]) 
                        
            df['PMID']=df['PMID'].astype(float).astype(int)
            if df['PubChem ID'][0] != None:            
             df['PubChem ID']=df['PubChem ID'].str.replace('NCT*.*','')
             df['PubChem ID']=df['PubChem ID'].str.replace(', *.*','')

             df['PubChem ID']=df['PubChem ID'].astype(float).astype(int)

            df.to_csv("test_datasets.csv",index=False)
            df1=df.transpose().reset_index()
            df1.columns=['Properties','Information']
            df1.drop(index=df1.index[:1], axis=0, inplace=True)
            df1 = df1.fillna(value='NA')
            Phytochemical=df["Phytochemical name or plant extracts"].values[0]


            #df1=df1.drop([0,2])
            print (df1)          
            return render_template('jatayu2_results.html',Phytochemical=Phytochemical,df1=df1, tables=[df1.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )
                

        



    return render_template("gene.html")




@app.route("/phytochemical")
def phytochemical():

    db=get_db()
    
    my_var = request.args.get('my_var', None)
    Phytochemical=my_var
    cur=db.execute('select  * from phyto_chemicals where Phytochemicalextract_name=?',[Phytochemical])
    results=cur.fetchall()
    print (results)
    df1=pd.DataFrame(results)
    print(df1)
    if not results:
            flash ('Something went wrong!','error')
            flash ('The entered Phytochemical name is not valid !!','info')

            return redirect(url_for('phytochemical'))
            
    else:
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" , "Phytochemical name or plant extracts" , "PMID" , "Literature evidence" , "IUPAC name" , "Phytochemicals’ class or type of plant extracts" , "Source of phytochemicals or plant Extracts","Geographical availability","Plant parts","Other cancers","Target gene or protein","Gene or Protein evidence","Target pathways","IC50","Potency","Study type","Additional information ","PubChem ID","Additional PMIDs","Additional sources of information","Safety"]) 
            df['Source of phytochemicals or plant Extracts']=df['Source of phytochemicals or plant Extracts'].str.replace(r"\(.*\).*","")
            df['PMID']=df['PMID'].astype(float).astype(int)
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           
            if df['PubChem ID'][0] != None:            
             df['PubChem ID']=df['PubChem ID'].str.replace('NCT*.*','')
             df['PubChem ID']=df['PubChem ID'].str.replace(', *.*','')
             df['PubChem ID']=df['PubChem ID'].astype(float).astype(int) 

            df.to_csv("test_datasets.csv",index=False)
            df1=df.transpose().reset_index()
            if len(df1.columns) == 3 :
             df1.columns=['Properties','Information1','Information2']
             #df1.drop(index=df1.index[:1], axis=0, inplace=True)
             df1 = df1.fillna(value='NA')
            else :
             df1.columns=['Properties','Information']
             #df1.drop(index=df1.index[:1], axis=0, inplace=True)
             df1 = df1.fillna(value='NA')


            
            """
            #df = pd.DataFrame(results, columns =[ "S. No." ,"Phytochemical_nameextract" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df = pd.DataFrame(results, columns =[ "S. No." ,"Phytochemical name/extract" , "PMID" , "Evidence" , "IUPAC name" , "Type of phytochemicals/Extracts" , "Source of phytochemicals (Name of Plant)","Geographical availability","Plant parts","Type of cancer","Target gene/ Protein","Gene / Protein evidence","Target pathway","IC50","Potency","Cell line/ mice model","ADDITIONAL INFO. ","PUBCHEM ID","ADDITIONAL PMIDs","ADDITIONAL SOURCES OF INFORMATION","Safety"])
            #df.to_csv("test_datasets.csv",index=False)
            df['PMID']=df['PMID'].astype(float).astype(int)
            if df['PUBCHEM ID'][0] != None:            
             df['PUBCHEM ID']=df['PUBCHEM ID'].astype(float).astype(int)

            df1=df.transpose().reset_index()
            df1.columns=['Properties','Information']
            df1.drop(index=df1.index[:1], axis=0, inplace=True)
            """

            #df1=df1.drop([0,2])
            print (df1)
            return render_template('jatayu2_results.html',Phytochemical=Phytochemical,df1=df1, tables=[df1.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )

   # dfjson=session.get("dfjson",None)
    #df = pd.read_json(dfjson, orient ='index')
    #print(df)
    #Phytochemical=df[['Phytochemical_nameextract']]
#    return render_template('jatayu2_results.html',Phytochemical=Phytochemical, tables=[df.to_html(classes='primer',index=None) ],
 #         titles = [ 'na' ,'Primers'] )


    #return render_template("second.html",d=d)

@app.route("/alphabatical", methods=['GET', 'POST'])
def alphabatical():
    return render_template("alphabets.html")


@app.route("/table", methods=['GET', 'POST'])
def table():
    alpha = request.args.get('alpha', None)

    alphabet=str(alpha)
    db=get_db()
    alphabetname=alphabet
    alphabet=alphabet+'%'
    print(alphabet)
    print("ALPHABET TYPE :", type(alphabet))

    #cur=db.execute('select  * from phyto_chemicals where ?  Like ?',('Phytochemical_nameextract', alphabet))
    cur=db.execute('select  * from phyto_chemicals where Phytochemicalextract_name  Like ?', [alphabet])

    results=cur.fetchall()
    #print (results)
    df1=pd.DataFrame(results)
    print(df1)

    if not results:
            flash ('Something went wrong!','error')
            flash ('There is not Phytochemical with this letter in the database !!','info')

            return redirect(url_for('alphabatical'))
            
    else:
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           
            selectdf=df[["PhytoCAT-ID","Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  

            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
            Feature=  "Phytochemicals with letter : "+ alphabetname
            selectdf = selectdf.fillna(value='NA')

            selectdf.columns=[  "PhytoCAT-ID" ,"Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  

            #selectdf.columns=["Phytochemical name/extract","Source of phytochemicals (Name of Plant)","Target gene/ Protein"]  

            return render_template('plants_results.html',Feature= Feature, selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )
                

        



    return render_template("alphabets.html")


#@app.route("/catagory", methods=['GET', 'POST'])
#def catagory():
#    return render_template("alphabets.html")


@app.route("/catagory", methods=['GET', 'POST'])
def catagory():
    catagory = request.args.get('catagory', None)

    catagory=str(catagory)
    db=get_db()
    alphabetname=catagory
    catagory='%'+catagory+'%'
    print(catagory)
    print("catagory TYPE :", type(catagory))
    
    if alphabetname == "Miscellaneous" :
        cur=db.execute('select  * from phyto_chemicals' )
        results=cur.fetchall()
        print (cur)
        df1=pd.DataFrame(results)
        print(df1)

        if not results:
            flash ('Something went wrong!','error')
            flash ('There is not Phytochemical with this letter in the database !!','info')

            return redirect(url_for('index'))
            
        else:
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           
            print (df['Type_of_phytochemicalsExtracts'])
            #print(df[df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|lactone|coumarin|terpenoid")])
            #df= df[~df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|Sesquiterpene lactone|Coumarin|Terpenoid")]
            df=df[~df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|Sesquiterpene lactone|Coumarin|terpen|Flav|Essential|extract|saponin|Triterpenoid saponin|Lignan|Quinone|Xanthone",na=False,case=False)]


            selectdf=df[['PhytoCAT-ID',"Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  

            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
            Feature=  "Phytochemicals Category : "+ alphabetname

            selectdf = selectdf.fillna(value='NA')

            selectdf.columns=['PhytoCAT-ID',"Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  


            return render_template('plants_results.html',Feature= Feature, selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )
    
    elif alphabetname == "Unknown" :
        cur=db.execute('select  * from phyto_chemicals where Type_of_phytochemicalsextract  is NULL')
        results=cur.fetchall()
        print (cur)
        df1=pd.DataFrame(results)
        print(df1)

        if not results:
            flash ('Something went wrong!','error')
            flash ('There is not Phytochemical with this letter in the database !!','info')

            return redirect(url_for('index'))
            
        else:
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           
            print (df['Type_of_phytochemicalsExtracts'])
            #print(df[df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|lactone|coumarin|terpenoid")])
            #df= df[~df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|Sesquiterpene lactone|Coumarin|Terpenoid")]
            #df=df[~df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|Sesquiterpene lactone|Coumarin|terpen|Flav|Essential|extract|saponin|Triterpenoid saponin|Lignan|Quinone|Xanthone",na=False,case=False)]


            selectdf=df[[ "PhytoCAT-ID" ,"Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  

            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
            Feature=  "Phytochemicals Category : "+ alphabetname
            selectdf = selectdf.fillna(value='NA')

            selectdf.columns=["PhytoCAT-ID","Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  
  

            return render_template('plants_results.html',Feature= Feature, selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )


    elif alphabetname == "All" :
        cur=db.execute('select  * from phyto_chemicals')
        results=cur.fetchall()
        print (cur)
        df1=pd.DataFrame(results)
        print(df1)

        if not results:
            flash ('Something went wrong!','error')
            flash ('There is not Phytochemical with this letter in the database !!','info')

            return redirect(url_for('index'))
            
        else:
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           

            print (df['Type_of_phytochemicalsExtracts'])
            #print(df[df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|lactone|coumarin|terpenoid")])
            #df= df[~df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|Sesquiterpene lactone|Coumarin|Terpenoid")]
            #df=df[~df['Type_of_phytochemicalsExtracts'].str.contains("alkaloid|Sesquiterpene lactone|Coumarin|terpen|Flav|Essential|extract|saponin|Triterpenoid saponin|Lignan|Quinone|Xanthone",na=False,case=False)]


            selectdf=df[[ "PhytoCAT-ID" ,"Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  

            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
            Feature=  "All Phytochemicals"
            selectdf = selectdf.fillna(value='NA')

            selectdf.columns=[ "PhytoCAT-ID" ,"Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  
  
            return render_template('plants_results.html',Feature= Feature, selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )
      



    else :
        cur=db.execute('select  * from phyto_chemicals where Type_of_phytochemicalsextract  Like ?', [catagory])
        results=cur.fetchall()
        print (cur)
        df1=pd.DataFrame(results)
        print(df1)

        if not results:
            flash ('Something went wrong!','error')
            flash ('There is not Phytochemical with this letter in the database !!','info')

            return redirect(url_for('index'))
            
        else:
            df = pd.DataFrame(results, columns =[ "PhytoCAT-ID" ,"Phytochemicalextract_name" , "PMID" , "Evidence" , "IUPAC_name" , "Type_of_phytochemicalsExtracts" , "Source_of_phytochemicals_Name_of_Plant" , "Geographical_availability" , "Plant_parts" , "Type_of_cancer" , "Target_gene_Protein" , "Gene__Protein_evidence" , "Target_pathway" , "IC50" , "Potency" , "Cell_line_mice_model" , "ADDITIONAL_INFO. " , "PUBCHEM_ID" , "ADDITIONAL_PMIDs" , "ADDITIONAL_SOURCES_OF_INFORMATION", "safety"]) 
            df['PhytoCAT-ID']='PhytoCAT-' + df['PhytoCAT-ID'].astype(str)           
            selectdf=df[[ "PhytoCAT-ID" ,"Phytochemicalextract_name","Source_of_phytochemicals_Name_of_Plant","Target_gene_Protein"]]  

            #dfjson = df.to_json(orient="index")
            #session["dfjson"]=dfjson
            Feature=  "Phytochemicals Category : "+ alphabetname
            selectdf = selectdf.fillna(value='NA')

            selectdf.columns=[  "PhytoCAT-ID" ,"Phytochemical name or plant extracts","Source of phytochemicals or plant Extracts","Target gene or protein"]  
  

            return render_template('plants_results.html',Feature= Feature, selectdf=selectdf, tables=[selectdf.to_html(classes='primer',index=None) ],
          titles = [ 'na' ,'Primers'] )
                

        



    return render_template("front1.html")


    


    

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(debug=True)
