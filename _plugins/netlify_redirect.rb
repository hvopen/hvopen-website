require "jekyll-redirect-from"

module JekyllRedirectFrom
  class Generator < Jekyll::Generator
    def generate(site)
      @site = site
      @redirects = {}

      # Inject our layout, unless the user has already specified a redirect layout'
      unless site.layouts.keys.any? { |name| name == "redirect" }
        site.layouts["redirect"] = JekyllRedirectFrom::Layout.new(site)
      end

      # Must duplicate pages to modify while in loop
      (site.docs_to_write + site.pages.dup).each do |doc|
        next unless JekyllRedirectFrom::CLASSES.include?(doc.class)
        generate_redirect_from(doc)
        # generate_redirect_to(doc)
      end

      generate_netlify
    end

    # For every `redirect_from` entry, generate a redirect page
    def generate_redirect_from(doc)
      doc.redirect_from.each do |path|
        page = RedirectPage.redirect_from(doc, path)
        redirects[page.redirect_from] = page.redirect_to
      end
    end

    def generate_netlify
      return if File.exist? site.in_source_dir("redirects.net")
      page = PageWithoutAFile.new(site, "", "", "redirects.net")
      page.content = ""
      @redirects.each do |from, to|
        page.content += "#{from} #{to}\n"
      end
      page.data["layout"] = nil
      site.pages << page

    end
  end
end
