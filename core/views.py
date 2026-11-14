from django.shortcuts import render, get_object_or_404
from .models import ActivityPost


def index(request):
    """
    Landing page for Layanan Kakak Asuh Vihara Vimala Dharma Bandung.
    Shows the hero section, stats bento grid, donation schemes,
    dynamic activity posts (with fallback if empty), testimonials, and FAQ.
    """
    activities = ActivityPost.objects.filter(is_published=True).order_by('-activity_date', '-created_at')[:9]
    
    # 6 Target Regions for Adik Asuh
    regions = [
        {"name": "Pati", "province": "Jawa Tengah", "icon": "🌾"},
        {"name": "Jepara", "province": "Jawa Tengah", "icon": "🪵"},
        {"name": "Ampel", "province": "Jawa Tengah", "icon": "⛰️"},
        {"name": "Wonosobo", "province": "Jawa Tengah", "icon": "🌄"},
        {"name": "Sukabumi", "province": "Jawa Barat", "icon": "🌊"},
        {"name": "Bandung", "province": "Jawa Barat", "icon": "🏛️"},
    ]
    
    # Testimonials from graduated Adik Asuh and Donors
    testimonials = [
        {
            "quote": "Bantuan dari para donatur melalui Kakak Asuh VVD memungkinkan saya menyelesaikan kuliah Sarjana Pendidikan tanpa terbebani tunggakan SPP. Sekarang saya bisa mengabdi mengajar anak-anak di daerah.",
            "author": "Sdr. W.P.",
            "role": "Adik Asuh Wisudawan (Pati)",
            "badge": "Lulusan S1 Pendidikan",
            "avatar_bg": "bg-amber-100 text-amber-800"
        },
        {
            "quote": "Sangat transparan dan personal. Setiap perkembangan nilai rapor dan kabar adik asuh saya selalu dikirim langsung via WhatsApp. Merasa tenang karena 100% donasi benar-benar tersalurkan tepat sasaran.",
            "author": "Ibu M.L.",
            "role": "Donatur Tetap Sejak 2021",
            "badge": "Donatur Rutin",
            "avatar_bg": "bg-blue-100 text-blue-800"
        },
        {
            "quote": "Terima kasih banyak Kakak Asuh PVVD. Ketika keluarga saya mengalami masa sulit, beasiswa ini hadir menjadi lentera sehingga saya bisa menyelesaikan SMK Jurusan Komputer dan langsung diterima bekerja.",
            "author": "Sdri. R.T.",
            "role": "Adik Asuh Wisudawati (Sukabumi)",
            "badge": "Lulusan SMK",
            "avatar_bg": "bg-emerald-100 text-emerald-800"
        }
    ]

    context = {
        'activities': activities,
        'has_activities': activities.exists(),
        'regions': regions,
        'testimonials': testimonials,
        'total_adik_asuh': 70,
        'region_count': 6,
    }
    return render(request, 'index.html', context)


def activity_detail(request, slug):
    """
    Dedicated detail page for an activity post (for direct links / SEO).
    """
    activity = get_object_or_404(ActivityPost, slug=slug, is_published=True)
    recent_activities = ActivityPost.objects.filter(is_published=True).exclude(pk=activity.pk).order_by('-activity_date')[:3]
    return render(request, 'activity_detail.html', {
        'activity': activity,
        'recent_activities': recent_activities,
    })

