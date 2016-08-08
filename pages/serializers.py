from pages.models import HomePage, HigherEducation, GeneralPage, ContactUs, AboutUs

from wagtail.contrib.wagtailapi.serializers import PageSerializer

class HomePageSerializer(PageSerializer):
    class Meta:
        model = HomePage
        fields = ('id',
                  'title',
                  'row_1',
                  'row_2',
                  'row_3',
                  'row_4',
                  'row_5',
                  'slug',
                  'seo_title',
                  'search_description',
                  )


class HigherEducationSerializer(PageSerializer):
    class Meta:
        model = HigherEducation
        fields = ('id',
                  'title',
                  'intro_heading',
                  'intro_description',
                  'row_1',
                  'get_started_heading',
                  'get_started_step_1_heading',
                  'get_started_step_1_description',
                  'get_started_step_1_cta',
                  'get_started_step_2_heading',
                  'get_started_step_2_description',
                  'get_started_step_2_cta',
                  'get_started_step_3_heading',
                  'get_started_step_3_description',
                  'get_started_step_3_cta',
                  'adopt_heading',
                  'adopt_description',
                  'adopt_cta',
                  'row_2',
                  'row_3',
                  'slug',
                  'seo_title',
                  'search_description',
                  )


class GeneralPageSerializer(PageSerializer):
    class Meta:
        model = GeneralPage
        fields = ('id',
                  'title',
                  'body',
                  'slug',
                  'seo_title',
                  'search_description',
                  )


class ContactUsSerializer(PageSerializer):
    class Meta:
        model = ContactUs
        fields = ('id',
                  'title',
                  'tagline',
                  'mailing_header',
                  'mailing_address',
                  'phone_number',
                  'slug',
                  'seo_title',
                  'search_description',
                  )


class AboutUsSerializer(PageSerializer):
    class Meta:
        model = AboutUs
        fields = ('tagline',
                  'intro_heading',
                  'intro_paragraph',
                  'our_team_heading',
                  'openstax_team',
                  'strategic_advisors',
                  'slug',
                  'seo_title',
                  'search_description',
                  )