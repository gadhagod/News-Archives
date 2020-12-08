module NewsArchives
    require "uri"
    require "net/http"
    require "json"

    class Non200Code < StandardError
    end

    $uri = URI.parse("https://newsarchives.herokuapp.com/api/v1")

    def NewsArchives.day(day)
        $uri.query = URI.encode_www_form({:day => day})
        res = JSON.parse(Net::HTTP.get($uri))
        if res["status"] == 200
            return res
        else
            raise Non200Code.new("The server responded with code #{res["status"]}: #{res["message"]}")
        end
    end

    def NewsArchives.month(month)
        $uri.query = URI.encode_www_form({:month => month})
        res = JSON.parse(Net::HTTP.get($uri))
        if res["status"] == 200
            return res
        else
            raise Non200Code.new("The server responded with code #{res["status"]}: #{res["message"]}")
        end
    end

    def NewsArchives.year(year)
        $uri.query = URI.encode_www_form({:year => year})
        res = JSON.parse(Net::HTTP.get($uri))
        if res["status"] == 200
            return res
        else
            raise Non200Code.new("The server responded with code #{res["status"]}: #{res["message"]}")
        end
    end

    def NewsArchives.keyword(keyword, day=nil, month=nil, year=nil, limit=nil)
        params = {:keyword => keyword}
        time_args = 0
        if day
            time_args = time_args + 1
            params[:day] = day
        end
        if month
            time_args = time_args + 1
            params[:month] = month
        end
        if year
            time_args = time_args + 1
            params[:year] = year
        end
        $uri.query = URI.encode_www_form(params)
        res = JSON.parse(Net::HTTP.get($uri))
        if res["status"] == 200
            return res
        else
            raise Non200Code.new("The server responded with code #{res["status"]}: #{res["message"]}")
        end
    end
end