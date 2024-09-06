import streamlit as st
import random

# Kelimeler ve tanımları
sozluk = {
"ALBARAN": "İspanya’dan gelen ürün kolilerinin takibinin yapılabilmesi için oluşturulan barkod",
    "AFLORADOS": "Sayımda okutulamayan fakat daha sonra stoğa dahil edilen ürünler",
    "AMOUNT": "Para birimi/ miktar",
    "ALARM OF SALE": "Merma kaynaklı çıkışıyapılan alarm tutarının totalsatışa oranı",
    "ACTIVE WAREHOUSE": "Reyonda sergilenen ürünlerin depoda bulunan stoğu",
    "ACTIVE PRODUCT": "Reyonda sergilenen ürün",
    "AREA": "Alan / Bölge",
    "AVERAGE TICKET": "Fiş başına düşen ortalama ürün adet satışı",
    "ART.TYPE (ARTICLE TYPE)": "Retail uygulamasında bulunan askı & katlı ürünlerin görüntülendiği seçenek",
    "ALERTS": "Uyarılar & Bildirimler",
    "ATTENDED": "Katılım onayı verildiğine dair uyarı & simge",
    "ALARM FINDER": "Bir ürünün bluebird cihazıyardımıyla bulunabilmesi için kullanılan özellik",
    "ARTICLE ALLOCATION": "Money Mapping uygulamasında bulunan, alanlara ürün ekleme / çıkarma yapılabilen ve daha önce eklenen ürünleri görmek için kullanılan fonksiyon",
    "ASSIGN": "Müşteri isteklerinin takibinde ürünün hangi lokasyona geleceğinin belirlenmesi için kullanılan fonksiyon / atama",
    "ALM.ACTIVO (ALMACEN ACTIVO)": "Aktif Depo",
    "ALM.PASSIVO (ALMACEN PASSIVO)": "Pasif Depo",
    "ALMACENES": "Depolar",
    "ADDED": "Deliveries uygulamasında görülen, planlanan sevkiyatta olmayan ancak faturalandırma sırasında sevkiyata eklenmiş ürünler",
    "ALARM DETAIL": "Alarm içerisine yüklü olan ürün bilgilerine bluebird yardımıyla ulaşılan fonksiyon",
    "ASSESSMENT": "Kişinin güçlü ve gelişime açık yönlerini belirlemek ve geliştirmek için yapılan değerlendirme",
    "AVERAGE SELLING PRICE (ASP)": "Bir ürünün ortalama satış fiyatı",
    "ATELIER TRAINING": "Campus ekibi tarafından verilen bir günlük rapor eğitimi",
    "AÑO": "Yıl",
    "BROKEN SIZE": "Bir ürünün en çok satan bedenlerinden en az bir tanesinin stoğunun tükenmesi",
    "BACKSTOCK": "Mağaza kapasitesi belirli birseviyenin üzerine çıktığında online depoya yapılan ürün transferi işlemi",
    "BACKSTOCK 1": "Mağazaya iade ile gelen tüm pasif ürünlerin online depoya yapılan ürün transferi işlemi",
    "BACKSTOCK 2": "Depo doluluk oranları belirli birseviyeye ulaştığında commercialveya yönetim ekibi tarafından ürünlerin belirli filtrelere göre liste oluşturularak Sertrans depoya gönderilmek üzere yapılan ürün transferi işlemi",
    "BACKSTOCK 3": "Depo doluluk oranları belirli birseviyeye ulaştığında commercialveya yönetim ekibi tarafından ürünlerin belirli filtrelere göre liste oluşturularak Tuzla depoya gönderilmek üzere yapılan ürün transferi işlemi",
    "BACKSTOCK 2/3": "Belirlenen ticari filtrelere göre herhangi bir liste oluşturmadan Sertrans depoya yapılan ürün transferi işlemi",
    "BACKSTOCK GUIDE": "Ürün müdürleri tarafından liste halinde gönderilen iade dışındaki left ürünlerinin çıkışının yapıldığı ürün transferi işlemi",
    "BLUEBIRD": "İçerisinde birden fazla uygulama bulunan, tüm RFID işlemlerinin yapılmasınısağlayan cihaz",
    "BOOST": "Retail uygulamasında in-store action kısmında twin mağazaların satış başarısı yakaladığı, mağazada reyonda sergilenen ancak display adetive ticari konumlandırma açısından kontrol edilmesi gereken ürünler",
    "BUYER": "Ürünlerin departmanlarına göre ayrılması Kadın: Woman / Basic / Trf/ Circular/ Punto vb. Erkek: Man / Global/ Denimwear/ Circularvb. çocuk: Boy/Girl/ Kids - A / Kids - O vb.",
    "BABY": "Yenidoğan (0-18 ay)",
    "BURRO": "Kolete göre ürün kapasitesi daha yüksek olan orta mobilya",
    "BASIC CLOTHES": "Hiçbir sezon değişmeyen, sade, zamansız kıyafetler",
    "BUENOS DIAS": "Mağaza açılmadan önce günün hedeflerinin ve gündeminin paylaşıldığı günaydın toplantısı",
    "BUNDLE": "Gelen ürün kolilerinin üzerindeki numara etiketleri",
    "BLASIER": "Blazer",
    "BERMUDA": "Şort",
    "BAR": "Askılı ürünleri taşımak için kullanılan tekerlekli metal yapı",
    "CONFIRMATION": "Ürün teslimatıve transfer çıkışlarının bluebird aracılığıyla onaylanması",
    "CLICK & GO": "Müşterilerin online uygulama üzerinden mağaza deposunda bulunan bir ürünü satın aldıktan 2 saat sonra mağaza içerisinden teslim alabilmesini sağlayan online uygulama fonksiyonu",
    "CLICK & TRY": "Müşterilerin online uygulama üzerinden 15 dakika süresince kabin rezerve etme işlemi",
    "CLICK & FIND": "Müşterilerin online uygulama üzerinden mağazada bulunan ürünlerin lokasyonlarını görebildikleri özellik",
    "COMPRAN & CONVERSION": "Müşterinin satışa dönüşümü hesaplanırken sadece satışiçin kesilen fişlerin dahil edildiği oran",
    "CONVERSION RATE": "Müşterinin satışa dönüşümü hesaplanırken satışve iade için kesilen fişlerin dahil edildiği oran",
    "CHANGEMAKER": "Mağazalarda sürdürülebilirlik aksiyonlarınıyönetmek için oluşturulan proje ve bu kapsamda her mağazada bulunan sürdürülebilirlik elçisine verilen isim",
    "CONTRIBUTION": "Satış içerisindeki ağırlık / Pay",
    "CORRECTION": "Bluebird ile ürünün stok bilgilerini düzeltme işlemi",
    "CM": "TGT üzerinden günlük ve saatlik shopfloor & stockroom hareketlerinin görüntülenebildiği alan",
    "COVERAGE": "Mağazanın mevcut satış hızı ile hiç ürün almadan elindeki ürün stoğunu kaç günde bitireceğini gösteren veri",
    "COMMERCIAL GROUP": "Buyer ayırmadan, ürünleri türlerine göre gruplama Pantolon / Dış Giyim / Gömlek / Tişörtvb.",
    "CUT LIST": "İndirim döneminde ürünlere uygulanacak fiyat listesi",
    "CHECK": "Kontrol etmek",
    "CIRCULAR": "Felpa ve tişört benzeri ürün gruplarının bulunduğu departman",
    "CROSS SELLING": "Müşterilerin aldığı ürünü tamamlar nitelikte farklı bir ürün grubunu tavsiye ederek satışı desteklemek/ Çapraz satış",
    "COLETTE": "Orta alanlarda ürün sergilemek için kullanılan mobilya",
    "CREATE EXPEDITION": "Sint siparişleri kargo görevlisine teslim edildikten sonra siparişlerin bir özetini gösteren ve imzalanarak görevliye teslim edilen belge",
    "CLIENT ENTRANCE": "Mağazaya girişyapan müşteri sayısı",
    "CLIENTES OPORTUNIDAD": "Mağazaya giriş yapan ve mağaza içerisinde herhangi bir işlem gerçekleştirmeyen müşterisayısı & oranı (Fırsat Müşteri)",
    "COMPRAN & DEVUELVEN": "Satış & İade",
    "COMPRAN IPOD": "Ipod satışı",
    "CLIENTES COMPRAN": "Alışveriş yapan müşteri",
    "CLIENTES QUE COMPRAN": "Fişteki ürün adeti dağılımı",
    "CLIENTES TIENDA": "Mağaza müşterisi",
    "CD1": "Haftada iki kez gerçekleşen ürün sevkiyatı",
    "CD2": "Günlük olarak gerçekleşen ürün sevkiyatı",
    "CAPACIDAD DEVO": "Depo kapasiteleri belirli birseviyenin üzerine çıktığında ürün müdürünün hazırladığı liste üzerinden yapılan transfer işlemi",
    "CAPACIDAD ALMACEN ONLINE": "Mağaza içerisinden müşteriye teslim edilecek online siparişlerin depolama alanı",
    "CLICK & COLLECT": "Mağazadan teslim edilecek online siparişsüreçlerinin genel adı",
    "CANCELADOS POR EL CLIENTE": "Müşterinin satın aldıktan sonra iptal ettiği online sipariş",
    "CONFE (CONFECCION)": "Depoda askılı olarak bulunan ürün",
    "COBERTURA TIENDA": "Mağaza içerisinde personelin hakim olduğu ortalama M2",
    "COBERTURA CLIENTE": "Mağaza içerisinde personelin yardımcı olduğu ortalama müşteri sayısı",
    "CAJAS": "Kasa",
    "CAMISA": "Gömlek",
    "COVERAGE ALARM": "Hırsızlık sebebiyle sistem üzerinden alarm çıkışıyapılan ürünlerin toplam kayıp içerisindeki oranı",
    "COVERAGE AFLORADOS": "Sayım sonrasında stoğa dahil edilen ürünlerin total kayıp oranı içerisindeki payı",
    "CABALLERO": "Erkek",
    "CLIENTE": "Müşteri",
    "CANCELLED": "Deliveries uygulamasında görülen, planlanan sevkiyatta olan ancak faturalandırma aşamasında sevkiyattan çıkarılan ürünler",
    "CHANGED AFTER PREVISION": "Deliveries uygulamasında yer alan,sevkiyat faturalandırıldıktan sonra gerçekleşen değişikliklerin görüntülendiği filtre",
    "COMPLEMENTOS (COMP)": "Aksesuar",
    "CARE FOR WATER": "Üretim aşamasında daha azsu kullanılarak üretilen giysilerde bulunan etiket",
    "CARE FOR PLANET": "Üretim aşamasında doğaya daha az kimyasal madde salınımıyapılarak üretilen giysilerde bulunan etiket",
    "CARE FOR FIBER": "Daha sürdürülebilir hammaddelerden en az biri kullanılarak üretilen giysilerde bulunan etiket",
    "CURRENT LOCATION": "Money Mapping uygulamasında zone içerisine en son tanımlanan ürünlerin bir haftalık satışını gösteren analiz",
    "CAMION": "Ürün sevkiyatı",
    "CONFIGURE SECTION": "Money Mapping uygulamasında mağaza içerisindeki alanları, mobilyaları eklediğimizve düzenleme yapabildiğimiz kısım",
    "CTA (CAMISETA)": "Tişört",
    "COMMERCIAL": "Kadın, erkek ve çocuk bölümlerindeki ticari ürün sorumlulularınına verilen genel ad",
    "CUSTOMER OPORTUNITY": "Mağazaya giriş yapıp herhangi bir işlem (ürün satın alma, iade vb.) yapmayan, satışa dönüştürülebilecek fırsat müşterileri",
    "CUSTOMER COVERAGE": "Bir ekip üyesinin ilgilendiği ortalama müşteri sayısı",
    "CUSTOMER EXPERIENCE": "Müşteri deneyimi",
    "CLOTHES": "Tekstil",
    "CAPACITY LIMIT": "Sint siparişleri maksimum kapasiteye ulaştığında mağazaya düşecek olan sipariş adeti",
    "CUSTOMER ENTRY": "Mağazaya giren kişi sayısı",
    "CAPSULE TRAINING": "Campus ekibi tarafından verilen bir günlük rapor eğitimi",
    "CALZADO": "Ayakkabı - Çanta / Tempe ürün grubu",
    "COACH": "Yeni ekip üyelerinin eğitimlerinde onlarla birlikte ilerleyerek eğitim veren kişilere verilen isim",
    "DENSITY": "M2 başına ortalama ürün adeti",
    "DISPLAY": "Bir ürünün reyonda sergilenme adeti",
    "DEVO": "Çeşitli sebeplerden ürün müdürü tarafından belirlenen ürünlerin merkez depoya transferinin yapılması",
    "DOUBLE": "Çift & Bir ürünün iki farklı alanda sergilenmesi",
    "DEAR TEAM": "Inet uygulaması üzerinden şirket içi haberlere, günlük toplantı konularına erişim sağlanabilen kısım",
    "DOUBLE HANGER": "Askı ürünlere takılan, tek askıda iki ürün depolanmasınısağlayan, depo kapasitesini arttırmak için kullanılan kırmızı ve plastik yapıdaki materyal",
    "DESCRIPTION": "Tanımlama",
    "DEVUELVEN": "İade",
    "DEVUELVEN.COM / DEVO @": "Online uygulamadan satın alınan ürünün mağazadan iade işlemi",
    "DEVO T.F. (DEVOLUCION TIENDA FISICA)": "Mağazadan satın alınan bir ürünün yine mağazadan iade işlemi",
    "DEVOLUCIONES AL ALMACEN": "Devo türleri",
    "DESTOCAJE": "Backstock",
    "DESDE ALMACEN E-COM": "Online depodan gelen siparişlere verilen genel isim",
    "DESTE TIENDA": "Mağazalardan transfer edilen siparişlere verilen genel isim",
    "DESESTIMADOS": "İptal edilen sipariş",
    "DOUBLE REFERENCE": "Bir ürünün birden fazla barkoda sahip olması",
    "DELIVERY": "Mağazaya gelecek olan ürün sevkiyatı",
    "DECODE": "Ürüne ait bilgilerin kayıtlı olduğu alarm içerisinden bu bilgilerin bluebird yardımıyla silinmesi işlemi",
    "DEVICE MANAGEMENT": "Mağaza içerisinde kullanılan teknolojik cihazların giriş, çıkışvb. işlemlerinin yönetimi",
    "DIRECTOR": "Mağazanın yönetim işlerinden sorumlu üst düzey yönetici/ Mağaza müdürü",
    "DISMISSED": "İptal edilen sipariş",
    "DEPORTIVO": "Spor ayakkabı",
    "EXPO & EXPUESTO": "Ürünlerin reyonda sergilenme oranı",
    "EXTERNAL": "Mağazanın dışında bulunan depo türlerine verilen genel isim",
    "ENTRANCE & ENTRADAS": "İçeri giren kişisayısı",
    "EAS (ELECTRONIC ALARM SYSTEM)": "Elektronik Alarm Sistemi/ Ürünlere ait bilgilerin gri alarmlara tanımlanmasıyerine içerisindeki etiklerde bulunan sticker alarmlara tanımlandığı teknolojik sistem",
    "ESTIMATION": "Tahmini",
    "EXPIRED": "Süresi biten",
    "EXTRA ONLINE": "Online paketlerin belirli birsüre müşteriler tarafından teslim alınmaması sebebiyle siparişin iptal edilerek ürünlerin mağaza stoğuna alınması işlemi",
    "ENVANTER": "Mağaza içerisinde kullanılan tüm materyaller",
    "EXTRANJERO": "Store map raporunda sisteme yabancı turist olarak kaydedilen müşteri verisi",
    "ENTREGADOS AL CLIENTE": "Müşteriye teslim edilen online paket",
    "EMPAQUETADOS": "Paketlenen sint siparişi sayısı",
    "ENTREGA ONLINE": "Online paket teslimatı",
    "ENCODE": "Ürüne ait bilgilerin alarm içerisine bluebird yardımıyla tanımlanması işlemi",
    "FRONTAL": "Duvarlarda öne doğru, kombin olarak sergilenen ürünler",
    "FOLDED": "Katlı ürünler",
    "FOUND": "Müşteri ürün isteğiyapıldıktan sonra, ürün operasyon ekibi tarafından depoda bulununca sisteme yapılan giriş & bildirim",
    "FELPA": "Peluşve yumuşak kumaşlara sahip ürünlere verilen isim (sweatshirt & tişört & taytvb.)",
    "FAULTY .COM": "Mağazada satışa uygun fakat online sipariş için uygun olmayan ürünlerin sipariş iptal çeşidi",
    "FAULTY STORE": "Mağaza ve online satışa uygun olmayan ürünler için belirlenen siparişiptal çeşidi",
    "FUERA DE TIEMPO": "Geciken online sipariş",
    "FOLDED ARTICLE": "Money Mapping uygulamasında Perimetral (duvar) mobilyasında katlı kullanılan ürünleri ayrıca belirtmek ve display değişiklikleri için kullanılan alan",
    "FITTING ROOM": "Prova Odası ( Kabin )",
    "FALDA": "Etek",
    "FAULTIES": "Müşteriye satış için uygun olmayan ve zarar görmüş ürünlere verilen genel isim",
    "FIND BUNDLE VIA RFID": "Ürün sevkiyat kolileri üzerindeki etiket düştüğünde veya okunmayacak durumda olduğunda bluebird yardımıyla okutarak ürünleri mağaza stoklarına dahil etmek",
    "FOREING TOU. (FOREIGN TOURIST)": "Store map raporunda sisteme yabancı turist olarak kaydedilen müşteri verisi",
    "GASTOS": "Mağaza bütçesine harcama olarak işlenen tüm gider biçimleri",
    "GASS (CONFIRMATION)": "Belirli sebeplerle stoğa alınamayan ürünlerishopfloor & stockroom hareketiyle otomatik olarak teslim alan sistem",
    "GAP": "Satış varyasyonu ile içeri giren kişi sayısı varyasyonu arasındaki fark",
    "GAP UNIDADES": "Adet satış varyasyonu ile içeri giren kişisayısı varyasyonu arasındaki fark",
    "GAP IMPORTES": "Para satış tutarı varyasyonu ile içeri giren kişisayısıvaryasyonu arasındaki fark",
    "GENERAL RETURN": "Ürün müdürü tarafından belirlenen ürünlerin tüm Türkiye’deki mağazalardan İspanya’ya gönderildiği bir devo türü",
    "GLORY": "Müşterinin nakit ödeme yöntemi ile işlemlerini kendisinin yaptığı kasa sistemi",
    "GREEN WAREHOUSE": "Yeşil (Aktif) depo / Reyonda sergilenen ürünlerin depoda bulunan stoğu",
    "GROSS SALE UNITS": "Brüt adet satışı",
    "GROSS SALE AMOUNT": "Brüt satış tutarı",
    "HANGING": "Askılı olan ürünlere verilen genel isim",
    "HARD TAG": "Açık gri renkli ve diğerlerine göre daha sert,sağlam yapıda olan kemik alarm",
    "HRS. TRABAJADAS (HOURS TRABAJADAS)": "Çalışma saati",
    "HRS. TOTALES (HOURS TOTALES)": "Gerekli kontrolleryapıldıktan sonra gün, hafta, ayveya yıl içerisinde kullanılan çalışma saatlerinin tamamı & onaylanması",
    "HOMBRE": "Erkek",
    "HOLD": "Ürünü bluebird aracılığıyla reyon ve depo stoklarından ayırıp rezerve etmek",
    "HIGHEST ENTRANCE": "En yüksek girişsayısına sahip olan mağazalara verilen genel isim",
    "HEALTH & SAFETY": "İş Sağlığıve Güvenliği",
    "HR (HUMAN RESOURCES)": "İnsan kaynakları",
    "HANDS OFF": "Campus ekibi tarafından ticari raporlar hakkında verilen bir haftalık rapor eğitimi",
    "INITIAL": "Bir ürünün mağazaya ilk giriş yaptığı stok adetleri",
    "INTERNAL STOCKROOM": "Mağaza içerisinde bulunan depolar",
    "INOX": "Kabinlerde ürünleri asmak, taşımak için kullanılan dar, uzun, tekerlekli metal bar",
    "IST (INTERNAL STOCKROOM)": "External depo kullanan mağazaların aktif ürünlerinin bir kısmının mağaza içerisinde bulunan iç depoda stoklanacak adetlerinin belirlenme işlemi",
    "INSUFFICIENT STOCK": "Yetersiz stok",
    "IMPORTES": "Para Birimi/ TL",
    "INFERIOR": "Sint alt limiti",
    "INVENTORY": "Envanter",
    "INBOUND": "Girişler (Ürün / Envanter)",
    "JOIN LIFE": "Sürdürülebilir yöntemler ile üretilmiş olan ürünleri belirtmek amacıyla oluşturulmuş proje ve etiket türü",
    "JUMPER": "Bir mağazanın herhangi birsebeple sintsiparişini iptal etmesive siparişin hazırlanmak için başka bir mağazaya düşmesi",
    "JERSEY": "Triko",
    "JOVEN": "Genç",
    "JUMPSUIT": "Tulum",
    "KNIT": "Triko/Örgü",
    "KPI": "Bir işletmenin durumunu analiz edebilmek için belirlenen anahtar performans göstegeleri",
    "KIDS-A": "Kız bebek",
    "KIDS-O": "Erkek bebek",
    "LEFT": "Total stoğu üç veya daha az olan ürün",
    "LATERAL": "Duvarlara ürünlerin yana bakacak şekilde sergilenmesi",
    "LOCKED": "Kilitli ürün",
    "LABEL": "Etiket",
    "LAYOUT": "Mağazada bölümlerin, koleksiyonların düzeni/ planı",
    "LENCERIA (LINGERIE)": "İç çamaşırı & Pijama",
    "LOSS PREVENTION SPACE (LPS)": "Power BI uygulaması içinde mağaza kayıplarını analiz ederek aksiyon almaya olanak sağlayan rapor",
    "LOCAL": "Alan, bölge / Store map raporunda sisteme mağazanın bulunduğu ilçe olarak kaydedilen müşteri verisi",
    "MERMA": "Mağaza içerisinde çalıntı, hatalı ürün transferivb.yollarla kayba sebep olan ürünlerin tümü",
    "MODO TIENDA": "Online uygulamanın mağaza ile entegrasyonunu sağlamaya yarayan özellik / mağaza modu",
    "MUST HAVE": "Reyonda mutlaka olması gereken, kilitlenemeyen ürün",
    "MOVE": "Mağazalar arasında yapılan ürün transferleri",
    "MARKET": "Ülkedeki tüm mağazalar",
    "MCC (MODEL/ QUALITY/ COLOUR)": "Ürünlere ait, sırasıyla model / kalite / renk bilgilerini içeren referans numaraları",
    "MONEY MAPPING": "Mağazanın ticari haritası",
    "MERCHAN MANAGER": "Koleksiyon fotoğraflarının ve ürün bilgilerinin yer aldığı uygulama",
    "MANAGE PERMISSION": "Yöneticilere çeşitli alanlara erişim sağlamaları için TGT üzerinden verilen izin yönetim alanı",
    "MATCHING": "Sint organizasyonunda siparişe ait ürünleri eşleştirme işlemi",
    "METS": "Mağazalar arası transfer",
    "MYSTORE": "Bir online siparişin aynı mağazadan hem stok çıkışının hem de teslim edilme işleminin yapılabildiği sipariş türü",
    "MONO": "Aynı model/ quality referans numarasına sahip en az iki rengi olan ürün grupları",
    "MESA": "Masa",
    "MUJER": "Kadın",
    "MODIFIED": "Deliveries uygulamasında sevkiyatla gelen ürünler için uygulanan hareketlerden etkilenen tüm ürünlerin göründüğü alan",
    "MINIMOS": "Bir subfamilyde belirlenmiş ve mağazada olması gereken minimum model sayısı",
    "MARK AS RECEIVED": "Bluebird üzerindeki ürün teslimat ekranında kolinin mağazaya varışyaptığını RFID yerine manual olarak işaretlemek",
    "MARK AS NON-RECEIVED": "Bluebird üzerindeki ürün teslimat ekranında kolinin mağazaya varışyapmadığını işaretlemek",
    "MISS BALANCE": "Bölümlerin satış payları ile depo stoğunda kapladıkları alanların birbirleriyle eş değer olmaması durumu",
    "MANIPULATION": "Bir adetlik satışiçin yapılan Rfıd hareketi sayısı",
    "NOTIFICATION": "Bildirim / Must- have olacak ürünler,satış oranlarına bağlı olarak sergileme adetlerinin arttırılması ya da azaltılması gereken ürünlerve reyonda yeterlistoğu olmayan ürünlere ait bilgilendirmeleri içeren ITX Stock bildirim ekranı",
    "NINA": "Kız çocuk (6-14 yaş)",
    "NINO": "Erkek çocuk (6-14 yaş)",
    "NASA": "Çöp poşeti takılan metal materyal",
    "NACIONAL": "Store map raporunda sisteme mağazanın bulunduğu ilden farklı bir il olarak kaydedilen müşteri verisi",
    "NO TEJANO": "Denim olmayan pantolon",
    "NOT REVIEWED": "Deliveries uygulamasında yer alan, herhangi bir planlama yapılmayan, gözden geçirilmeyi bekleyen ürünlerin görüntülendiği filtreleme",
    "NEGATIVE TENDENCY": "Ürün sevkiyatıyla gelecek olan replenishment adetinin azaltılması",
    "NOT FOUND": "Müşteri ürün isteğiyapıldıktan sonra, ürün operasyon ekibi tarafından depoda bulunamadığında sisteme yapılan giriş & bildirim",
    "NATIONAL TOU. (NATIONAL TOURIST)": "Store map raporunda sisteme mağazanın bulunduğu ilden farklı bir il olarak kaydedilen müşteri verisi",
    "OVERSTOCK": "Bir ürünün reyonda olması gerekenden fazla olan stoğu",
    "OMNICHANNEL": "Online mağaza ve fiziksel mağazaların stoklarının birbirlerine entegre ilerlemesini sağlayan kanal",
    "OCCUPACION": "Doluluk",
    "OTROS": "Diğer",
    "ONLINE INVENTORY": "Online siparişlerin mağaza içerisinde stoklanan adetleri",
    "OFFER": "Gestion Stock uygulaması içerisinde filtreleme yapılan alan",
    "OPERATION MANAGER": "Mağazanın operasyonel süreçlerinin yönetimiyle ilgilenen yönetici/ Operasyon müdürü",
    "OPERATION RESPONSIBLE": "Mağazanın operasyonel süreçlerinden sorumlu kişi/ Operasyon sorumlusu",
    "OUTBOUND": "Çıkışlar (Ürün / Envanter)",
    "ONLINE RECEPTION": "Online paket teslimi",
    "OUT OF TIME": "Geciken sint",
    "PASSIVE WAREHOUSE": "Reyonda sergilenmeyen ürünlerin olduğu depo",
    "PASSIVE PRODUCT": "Reyonda sergilenmeyen ve depoda olan ürün",
    "PICKING": "Online siparişler içerisindeki ürünlerin toplanması işlemi",
    "PACKING": "Online siparişlerin çıkış yapılarak paketlenmesi işlemi",
    "PENDING": "Online siparişler için toplanmayı bekleyen ürünler",
    "PRODUCTIVITY": "Verimlilik / Bir kişinin bir saatte yaptığı işin verimliliği",
    "PRESCRIBER CRITERIA": "Fiziki mağaza satışı ve ipod satış kriterlerini baz alan filtreleme",
    "PRINTER (Zebra ve Toshıba)": "Fiyat etiketlerinin çıktı alındığı cihaz",
    "PRODUCT": "Ürün",
    "PRODUCT TYPE": "Ürün Tipleri/ Tekstil & Tempe & Parfüm",
    "PLAN DISPLAY": "TGT üzerinden ürünlerin toplu birşekilde kilit açma & kapatma, display arttırma & azaltma hareketlerinin yapılabildiği alan",
    "PVP": "Yeni sezon ürünlere uygulanan promosyon ile fiyatlarının düşmesi/ Promosyonlu Ürün",
    "PUNTO": "Triko grubuna dahil olan tüm ürünler",
    "PLUSH": "Peluş ve yumuşak kumaşlara sahip ürünlere verilen isim (sweatshirt & tişört & taytvb.",
    "PLEXI": "Fiyat görsellerinin içine koyulduğu sert, plastik materyal",
    "PERSONNEL CODE": "Çalışanların şirketteki kimlik numarası",
    "PEOPLE COUNTER": "Kapılarda bulunan ve içeri giren kişilerisayan cihaz",
    "PRIORITY REMOVEL": "İspanya tarafından satışı yasaklanmış ve bekletilmeden çıkışı yapılması gereken ürünler",
    "PROMO": "Promosyonlu ürünlerveya black friday ürünleri",
    "PREPERATION": "Ürün günü öncesiyapılan display ayarlama, lokasyon belirleme vb. tüm hazırlık işlemleri",
    "P&L": "Bir işletmenin belirli bir döneme ait gelir ve giderlerinden oluşan, kâr veya zararı gösteren mali tablo",
    "PICKING BY BUNDLE": "Öncelikli olarak reyona çıkması gereken ürünlerin açılıp etiketlerinin yapıldığı,sonrasında depoda olacak ürünler için planlamanın yapıldığı ürün açma sistemi",
    "PEDIDOS RECIBIDOS": "Teslim alınan online paket",
    "PEDIDOS ENTREGADOS": "Güncel online paket adeti",
    "PAQUETERIA (PAQUE)": "Katlı ürün",
    "PROPUESTA DE ENVIO": "Stoklardan çıkışyapılması gereken adet",
    "PLANTA & PROBA": "Reyon + Kabin",
    "PERIMETRAL": "Mağazada ürünlerin sergilendiği duvar mobilyaları",
    "P.EXT (PRENDA EXTERIOR)": "Dış Giyim",
    "P.PAQUE (PANTOLON PAQUE)": "Katlı Pantolon",
    "P.CONFE (PANTOLON CONFE)": "Askı Pantolon",
    "POLO": "Üst giyim ürünlerde gömleğe benzeryaka biçimi",
    "PERFU": "Parfüm",
    "PANTONE": "Tüm dünyada moda, tekstil, ev tekstili, endüstri tasarım, boya vb. gibi pek çok sektörde renk iletişimini doğru şekilde sağlamak için kurulmuşrenk sistemive tedarikçisi",
    "PRODUCT CARE": "Retail içerisinde in-store actions alanında bulunan ve stoklarda ütülenmesi gerekebilecek ürünlerin bulunduğu alan",
    "POSITIVE TENDENCY": "Ürün sevkiyatıyla gelecek olan replenishment adetinin arttırılması",
    "PRODUCT EXPERIENCE": "Ürün deneyimi",
    "PACKED AVERAGE TIME": "Mağazaya düşen sintsiparişinin ortalama paketlenme süresi",
    "PSP (PRODUCT SELLING PRICE)": "Bir ürünün ortalama satış fiyatı",
    "PETIS": "İstek",
    "PETIS VERDE": "Aktif Ürün İsteği",
    "PETIS ROJAS": "Pasif Ürün İsteği",
    "PETICIÓN DESBL": "Müşteri isteklerindeki aktif ürün oranı",
    "PETICIÓN DESBL PENTIENTES REPONER": "Müşteri isteği yapılıp aynı zamanda 25’te olan ürün yüzdesidir",
    "QUERIES": "ITX Stock uygulamasında “more” kısmından erişilen ve mağaza stoklarının belirli filtrelemeler yaparak görüntülenebileceği kısım",
    "REPLENISHMENT": "Mağaza stoklarına daha önce girişyapmış olan ürünlerin satan bedenlerinin, ürün sevkiyatı ile mağaza stoklarına tekrar girmesi",
    "ROTASYON": "Toplam stoğu 4 ve üzeri olan reyonda sergilenmeyen (pasif) ürünler",
    "REINFORCEMENT": "Belirli saat ve tarih aralıklarında satış potansiyeli olan ürünlerin displaylerini arttırmayısağlayan uygulama",
    "RUNNER": "Kabin dağıtımı yapan ekip üyelerine verilen genel isim",
    "RANKING": "Satış sıralaması",
    "REMOVEL": "İspanya tarafından çeşitli nedenlerle satışı yasaklanan ürünler",
    "RFID": "Radyo frekansteknolojisi kullanılarak tüm ürün hareketlerinin kaydedilmesini sağlayan sistem",
    "RECOVER": "Retail uygulamasında instore action kısmında bulunan reyonda sergilenmeyen ancak twin mağazaların reyonda sergilediği ve satış başarısı yakaladığı, depodan kurtarılabilecek potansiyel ürünler",
    "REMOVE": "Retail uygulamasında in-store action kısmında bulunan, reyonda sergilenen ama mağazada ve twin mağazalarda satış başarısı yakalayamayan depoya çekilebilecek ürünler",
    "RESCUE": "Pasif depodan reyona ürün çıkarmak, ürün kurtarmak",
    "REFERENCE": "Her ürüne ait model/ kalite /renk ve beden belirten kod",
    "REJECT": "Online siparişin çeşitlisebeplerden iptal edilmesi",
    "RETAIL": "Satış & stok analizinin yapılabildiği uygulama",
    "RECOGEN.COM": "Online paket teslimatı",
    "REGIONAL": "Store map raporunda sisteme mağazanın bulunduğu ilçe dışındaki farklı bir ilçeden olarak kaydedilen müşteri verisi",
    "RECOVER COMPOSITION": "Money Mapping uygulamasında bir zone içerisine daha önce okutulan ürünlerin görüntülendiği fonksiyon",
    "RECENTLY SCANNED": "ITX Stock uygulamasında en son okutulan ürünlerin görüntülebildiği alan",
    "RESTOS": "Total stoğu 4 adet olan ürün",
    "RECEIVED": "Deliveries uygulamasında yeni veya satış potansiyeli olan önemli ürünlerle alakalı yapılan tüm hareketlerin görüntülendiği alan",
    "RESEND TO PDA": "Confirme edilmiş albaranın confirmesinin iptal edilip tekrar teslimat ekranına gönderilmesi",
    "REPLENISHMENT RANKING": "25 çıkartma performans raporu",
    "RED WAREHOUSE": "Kırmızı (Pasif) depo / Reyonda sergilenmeyen ürünlerin olduğu depo",
    "RATIO": "Oran,yüzde",
    "ROPA": "Tekstil",
    "RECIBIDOS": "Mağazaya düşen SINT sipariş adeti",
    "RETURN PROPOSAL": "Depodan gönderilmesi gereken ürün adeti",
    "RC ASSIGN": "yapılan isteklerin satışa dönüşme oranı",
    "SHOPFLOOR": "Reyon Alanı",
    "STOCKROOM": "Depo Alanı",
    "SHOFLOOR LOCKED": "Reyonda 3 veya daha fazla adette olup kilitli olan ürünlerin görüntülendiği alan",
    "SINT": "Online üzerinden yapılan alışverişlerde mağazaya yansıyan siparişlerin paketlenip, kargolandığı süreç",
    "SHIFT": "Ekibin tüm üyelerinin haftalık çalışma tablosu",
    "SUBFAMILY": "Ürün grupları",
    "SUBTYPE": "Mağazada gerçekleşen satış türlerinin genel adı - In Store /Ipod / Sint",
    "SALES WEIGHT": "Satış payı / ağırlığı",
    "SECTION": "Bölümlere verilen genel ad",
    "STORE CRITERIA": "In store, Ipod ve Sint satış kriterlerinin dahil olduğu filtreleme",
    "SCAN": "Herhangi bir ürünü sistemde görebilmek için bir cihaz aracılığıyla okutmak",
    "SEEN": "ITX üzerinden müşteri için ürün isteğiyapıldığında isteğin karşı taraftan görüldüğüne dair bildirim",
    "STORE MAP": "Mağaza analiz raporu / mağaza analiz haritası",
    "SOFT TAG": "Etiket alarm",
    "SEPERATÖR": "Ürünleri türlerine ya da alınan aksiyon çeşidine göre birbirinden ayırmak için kullanılan plastik aparat",
    "STOCKTAKE": "Mağazadaki ürünlerin stok bilgilerini güncellemek ve kayıpları belirlemek amacıyla yapılan sayım organizasyonu",
    "SCO (SELF CHECK OUT)": "Müşterinin kredi kartı ile ödeme işlemlerini kendisinin yaptığı kasa sistemi",
    "SALIDAS": "Mağazadan gerçekleşen tüm stok çıkışlarına verilen genel isim",
    "SUPERIOR": "Sint satış işlemi için mağazanın satış ekranında görüntüleyebildiği üst limit",
    "SUDADERA": "Sweatshirt",
    "SENORA": "Kadın",
    "SHIPMENTS TO ZARA HOME": "Zara Home markasına ait ürünlerin çıkışının yapıldığı uygulama",
    "SET UP STOCKROOM": "Depo oluşturmak veya depo düzenlemek için kullanılan uygulama",
    "SPECIAL RETURN": "Online depoya gerçekleştirilen ürün transferleri",
    "SALES LOCATION": "Money Mapping uygulamasında rapor görüntülerken, herhangi bir zone içerisinde bir hafta boyunca tanımlanmış bütün ürünlerin satışverisini gösteren analiz",
    "SALES BREAKDOWN": "Retail uygulaması içerisinde satışın farklı şekillerde görüntülenebilmesini sağlayan fonksiyon",
    "SUB-DIRECTOR": "Mağaza direktörünü asiste eden üst düzey yönetici",
    "SECTION MANAGER": "Mağaza içerisindeki bölümlerden sorumlu yönetici/ Bölüm müdürü",
    "STORE COVERAGE": "Bir ekip üyesinin reyonda hakim olduğu ortalama metrekare",
    "SEMANA": "Hafta",
    "STOCK GESTION": "Stok yönetimi",
    "SHOWROOM": "Birden fazla tempe modelinin tek bir alanda sergilendiği yer",
    "TARA": "Müşteriye satış için uygun olmayan ve zarar görmüş ürünlere verilen genel isim",
    "TURNOVER": "İşyerinde çalışanların işten ayrılma oranı",
    "THEFT": "Hırsızlık sebebiyle bulunan alarm,stokta oluşan kayıp",
    "TIMETABLE": "Ekibin tüm üyelerinin haftalık çalışma tablosu",
    "TWIN STORE": "Mağazaya m2, satış ve stok kriterlerinde en çok benzerlik gösteren eş mağazalara verilen isim",
    "TGT": "Mağazanın birçok alanında ve yönetiminde kullanılan, bilgi alıp gönderilen, iletişim kurulan terminal",
    "TAKE BACK": "Kullanılmış tekstil ürünlerinin geri dönüştürülmesi amacıyla oluşturulan giysi toplama projesi",
    "TEMPE": "Ayakkabı ve çantalara verilen genel isim",
    "TICKET": "Satış sonrası kesilen fiş",
    "TAX-FREE": "İkameti Türkiye dışında olan müşterilerin alışverişlerinde kdv iadesi alabilmeleri için kesilen fiş",
    "TEMPE PAQUETERIA": "Kutulu ayakkabı",
    "TIEMPO ENTRE RECEPTION YENTREGA AL CLIENTE": "Sint ekranına yansıyan bir siparişin müşteriye ortalama teslimat süresi",
    "TIEMPO MEDIO EMPAQUETADO": "Sint ekranına yansıyan bir siparişin ortalama paketlenme süresi",
    "TEJANO": "Denim pantolon",
    "TRAJE": "Takım elbise",
    "TARGET": "Hedef",
    "TRANSFER TO SHOPFLOOR": "Ürünleri bluebird ile depodan reyona transfer etme işlemi",
    "TRANSFER TO STOCKROOM": "Ürünleri bluebird ile reyondan depoya transfer etme işlemi",
    "TRADE GROUPS ORDER": "25 uygulamasında ürünlerin türlerine göre sıralaması - pantolon / mont/tişört vb.",
    "TRANSFER OUT": "Mağazadan stok çıkışı yapılan tüm hareketlere verilen ortak isim",
    "TRANSIT PARTIAL DELIVERY": "sevkiyatta bir albaranda eksik koliler geldiğinde gelmeyen koliler için yeniden oluşturulan albaran (irsaliye)",
    "TUTOR": "Mağazanın eğitim süreçlerini takip edip, eğitim veren kişi",
    "TENDENCY": "Ürün sevkiyatındaki replenishment adetlerinde yapılan değişiklik",
    "TRADE MEASURES MANAGEMENT": "Gestion Stock uygulaması içerisinde bloklama, filtreleme, bloklanmış ürün ve bloktan silinmiş ürünlerin seçerek görüntülenebildiği alan",
    "TALENT POOL": "Campus ekibi tarafından özellikle People ve Process alanında verilen 3 haftalık eğitim",
    "TRUCK": "Ürün sevkiyatı",
    "TOTEM": "Dört adet küpten oluşan ve üzerinde tempenin sergilendiği mobilya",
    "TRAFFIC PROFIT": "Retail ana sayfada gördüğümüz GAP verisi",
    "URGENT": "acil /öncelikli",
    "UNIT & UNIDADES": "Adet",
    "UNIT PER TICKET / UDSxTICKET": "Fiş başına düşen ortalama ürün adeti",
    "URBANO": "Store map raporunda sisteme mağazanın bulunduğu ilçeden olarak kaydedilen müşteri verisi",
    "UMBRAL RELACION CAPACIDAD": "Mağazanın aldığı sint sipariş sayısı maksimum kapasiteye ulaştığında, mağazanın almaya devam edebileceği maksimum sipariş limiti",
    "VENTA": "Satış",
    "VSW (VISUAL SHOWROOM)": "Ürünlerin mağaza stoklarındayken online satışa sunulması için sistem üzerinden yapılan tanımlama işlemi",
    "VARIATION": "Kıyaslanan zamana göre değişim",
    "VISITS": "Mağazaya girişyapan kişi sayısı",
    "VENTA BRUTA": "Brüt satış",
    "VENTA UNIDADES": "Satış Adeti",
    "VENTA IMPORTES": "Satış Tutarı",
    "VENTA TIENDA FISICA": "Mağazadan gerçekleşen fiziki satış türü",
    "VESTIDO": "Elbise",
    "VOID": "Mağaza stoklarından çıkışı yapılan ürünlerin 14 gün içerisinde çıkış işleminin iptal edilmesi",
    "WEIGHT": "Ağırlık / Pay",
    "WAKE UP": "İndirim döneminde depoda olan ürünleri belirli bir şekilde ayırmayı amaçlayan uygulama 25'e yansıyan ürünlerin pasif depoda olduğunu anlamak amacıyla kurulur",
    "WAREHOUSE": "Depo",
    "WAREHOUSE REQUEST": "Depodan müşteri için yapılan ürün istekleri",
    "WELCOMER": "Mağazaların giriş alanlarında müşteriyi karşılayan ekip üyesi",
    "WAREHOUSE CONFIGURATION": "Ürünlerin depodaki konumlarının belirlendiği ve 25 R uygulamasında ürünlere subfamily sıralamasının yapıldığı yer",
    "YESTERDAY": "Bir önceki gün",
    "ZONE": "Mağaza içerisinde reyonda belirlenen alanlar",
    "ZARA FASHION WEEK": "Zara mağazaları için her sezon yapılan moda haftası etkinliği",
}

# Kelimeleri rastgele sıraya koy
kelimeler = list(sozluk.items())
random.shuffle(kelimeler)

# CSS stilini ekleyelim (Büyük kartlar ve animasyonlar)
st.markdown(
    """
    <style>
    body {
        background-color: #f0f4f8;
    }
    .card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        padding-top: 50px;
        padding-bottom: 50px;
        background-color: #d3f8e2;
    }
    .card {
        width: 400px;
        height: 400px;
        background-color: #ffcccb;
        margin: 15px;
        text-align: center;
        border-radius: 15px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        transition: transform 0.6s;
        transform-style: preserve-3d;
        position: relative;
        font-size: 28px;
        color: #333;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .flipped {
        transform: rotateY(180deg);
    }
    .card-front, .card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 15px;
    }
    .card-front {
        background-color: #f0e68c;
        color: #333;
    }
    .card-back {
        background-color: white;
        color: #333;
        transform: rotateY(180deg);
        padding: 20px;
    }
    </style>
    <script>
    function flipCard(id) {
        var card = document.getElementById(id);
        card.classList.toggle('flipped');
    }
    </script>
    """,
    unsafe_allow_html=True
)

# Kartlar konteynerini başlat
st.markdown('<div class="card-container">', unsafe_allow_html=True)

# Kartların render edilmesi
for i, (word, definition) in enumerate(kelimeler):
    card_id = f"card_{i}"
    
    # Kartın önü ve arkası
    st.markdown(f"""
    <div id="{card_id}" class="card" onclick="flipCard('{card_id}')">
        <div class="card-front">{word}</div>
        <div class="card-back">{definition}</div>
    </div>
    """, unsafe_allow_html=True)

# Kartlar konteynerini kapat
st.markdown('</div>', unsafe_allow_html=True)

# Yeni kelime seti oluşturma
if st.button("Yeni Kart Seti"):
    random.shuffle(kelimeler)
    st.experimental_rerun()
