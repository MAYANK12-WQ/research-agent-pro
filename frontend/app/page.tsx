'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Search, Sparkles, TrendingUp, BarChart3, FileText } from 'lucide-react';

export default function HomePage() {
  const [query, setQuery] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const router = useRouter();

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setIsSearching(true);

    // Simulate search delay
    setTimeout(() => {
      router.push(`/research?q=${encodeURIComponent(query)}`);
    }, 500);
  };

  const exampleQueries = [
    "AI startup funding trends in Europe 2024",
    "Compare iPhone vs Android market share in Asia",
    "Electric vehicle adoption by country",
    "Climate change impact on agriculture",
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900">
      {/* Header */}
      <header className="border-b border-white/10 backdrop-blur-sm bg-white/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Sparkles className="w-8 h-8 text-blue-400" />
              <h1 className="text-2xl font-bold text-white">Research Agent Pro</h1>
            </div>
            <a
              href="https://github.com/MAYANK12-WQ/research-agent-pro"
              target="_blank"
              rel="noopener noreferrer"
              className="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg text-white transition-all"
            >
              GitHub ⭐
            </a>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center space-y-8">
          {/* Hero Text */}
          <div className="space-y-4">
            <h2 className="text-5xl md:text-7xl font-bold text-white">
              Research anything,
              <br />
              <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                get insights instantly
              </span>
            </h2>
            <p className="text-xl text-slate-300 max-w-2xl mx-auto">
              The most sophisticated AI research agent with automatic charts, graphs, and infographics
            </p>
          </div>

          {/* Search Bar */}
          <form onSubmit={handleSearch} className="max-w-3xl mx-auto">
            <div className="relative group">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-500 rounded-2xl blur-xl opacity-50 group-hover:opacity-75 transition-opacity"></div>
              <div className="relative bg-white rounded-2xl shadow-2xl p-2">
                <div className="flex items-center">
                  <Search className="w-6 h-6 text-slate-400 ml-4" />
                  <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Ask me anything... (e.g., 'AI startup funding trends 2024')"
                    className="flex-1 px-4 py-4 text-lg outline-none text-slate-900"
                    disabled={isSearching}
                  />
                  <button
                    type="submit"
                    disabled={!query.trim() || isSearching}
                    className="px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-xl font-semibold hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {isSearching ? 'Searching...' : 'Research'}
                  </button>
                </div>
              </div>
            </div>
          </form>

          {/* Example Queries */}
          <div className="space-y-4">
            <p className="text-sm text-slate-400">Try these examples:</p>
            <div className="flex flex-wrap justify-center gap-3">
              {exampleQueries.map((example, index) => (
                <button
                  key={index}
                  onClick={() => setQuery(example)}
                  className="px-4 py-2 bg-white/10 hover:bg-white/20 border border-white/20 rounded-lg text-sm text-white transition-all"
                >
                  {example}
                </button>
              ))}
            </div>
          </div>

          {/* Features */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 max-w-4xl mx-auto">
            <div className="p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
              <TrendingUp className="w-12 h-12 text-blue-400 mb-4 mx-auto" />
              <h3 className="text-lg font-semibold text-white mb-2">Auto Charts</h3>
              <p className="text-slate-300 text-sm">
                Automatically generates line, bar, pie, and scatter charts
              </p>
            </div>

            <div className="p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
              <BarChart3 className="w-12 h-12 text-purple-400 mb-4 mx-auto" />
              <h3 className="text-lg font-semibold text-white mb-2">Infographics</h3>
              <p className="text-slate-300 text-sm">
                Beautiful infographics with key statistics and insights
              </p>
            </div>

            <div className="p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
              <FileText className="w-12 h-12 text-green-400 mb-4 mx-auto" />
              <h3 className="text-lg font-semibold text-white mb-2">Export Anywhere</h3>
              <p className="text-slate-300 text-sm">
                PDF, PowerPoint, PNG, Markdown - your choice
              </p>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-white/10 mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 text-center text-slate-400 text-sm">
          <p>Built with 💡 by <a href="https://github.com/MAYANK12-WQ" className="text-blue-400 hover:underline">Mayank</a></p>
          <p className="mt-2">100% Free & Open Source • Better than $20/month tools</p>
        </div>
      </footer>
    </div>
  );
}
