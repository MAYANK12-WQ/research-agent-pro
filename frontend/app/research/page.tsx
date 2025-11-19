'use client';

import { Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import { ArrowLeft, Download, Share2, Sparkles } from 'lucide-react';
import Link from 'next/link';
import { LineChart, Line, BarChart, Bar, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function ResearchPageContent() {
  const searchParams = useSearchParams();
  const query = searchParams.get('q') || 'AI startup funding trends';

  // Demo data for charts
  const trendData = [
    { year: '2020', funding: 25 },
    { year: '2021', funding: 42 },
    { year: '2022', funding: 68 },
    { year: '2023', funding: 95 },
    { year: '2024', funding: 127 },
  ];

  const countryData = [
    { country: 'United States', funding: 45 },
    { country: 'United Kingdom', funding: 28 },
    { country: 'Germany', funding: 18 },
    { country: 'France', funding: 15 },
    { country: 'Netherlands', funding: 12 },
  ];

  const sectorData = [
    { name: 'Healthcare AI', value: 35, color: '#3B82F6' },
    { name: 'FinTech AI', value: 28, color: '#8B5CF6' },
    { name: 'Enterprise AI', value: 22, color: '#10B981' },
    { name: 'Consumer AI', value: 15, color: '#F59E0B' },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900">
      {/* Header */}
      <header className="border-b border-white/10 backdrop-blur-sm bg-white/5 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <Link href="/" className="flex items-center space-x-2 text-white hover:text-blue-400 transition-colors">
              <ArrowLeft className="w-5 h-5" />
              <span>Back to Search</span>
            </Link>
            <div className="flex items-center space-x-3">
              <button className="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg text-white transition-all flex items-center space-x-2">
                <Share2 className="w-4 h-4" />
                <span>Share</span>
              </button>
              <button className="px-4 py-2 bg-blue-500 hover:bg-blue-600 rounded-lg text-white transition-all flex items-center space-x-2">
                <Download className="w-4 h-4" />
                <span>Export</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Query Title */}
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            {query}
          </h1>
          <div className="flex items-center space-x-4 text-sm text-slate-300">
            <span className="flex items-center space-x-1">
              <Sparkles className="w-4 h-4 text-blue-400" />
              <span>Research Complete</span>
            </span>
            <span>•</span>
            <span>24 sources analyzed</span>
            <span>•</span>
            <span>18.3 seconds</span>
          </div>
        </div>

        {/* Key Insights Infographic */}
        <div className="mb-8 p-8 bg-gradient-to-br from-blue-500/20 to-purple-500/20 border border-blue-500/30 rounded-2xl backdrop-blur-sm">
          <h2 className="text-2xl font-bold text-white mb-6 flex items-center">
            <Sparkles className="w-6 h-6 mr-2 text-yellow-400" />
            Key Insights
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center">
              <div className="text-5xl font-bold text-blue-400 mb-2">$127B</div>
              <div className="text-slate-300">Total Funding 2024</div>
            </div>
            <div className="text-center">
              <div className="text-5xl font-bold text-purple-400 mb-2">+43%</div>
              <div className="text-slate-300">YoY Growth</div>
            </div>
            <div className="text-center">
              <div className="text-5xl font-bold text-green-400 mb-2">2,847</div>
              <div className="text-slate-300">Active Startups</div>
            </div>
          </div>
        </div>

        {/* Charts Grid */}
        <div className="space-y-8">
          {/* Line Chart - Funding Trend */}
          <div className="p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
            <h3 className="text-xl font-semibold text-white mb-4">AI Startup Funding Over Time</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={trendData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                <XAxis dataKey="year" stroke="#94A3B8" />
                <YAxis stroke="#94A3B8" />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#1E293B',
                    border: '1px solid #334155',
                    borderRadius: '8px',
                    color: '#F8FAFC',
                  }}
                />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="funding"
                  stroke="#3B82F6"
                  strokeWidth={3}
                  dot={{ fill: '#3B82F6', r: 6 }}
                  activeDot={{ r: 8 }}
                  name="Funding ($B)"
                />
              </LineChart>
            </ResponsiveContainer>
          </div>

          {/* Bar Chart - Top Countries */}
          <div className="p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
            <h3 className="text-xl font-semibold text-white mb-4">Top Countries by Funding</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={countryData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                <XAxis dataKey="country" stroke="#94A3B8" />
                <YAxis stroke="#94A3B8" />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#1E293B',
                    border: '1px solid #334155',
                    borderRadius: '8px',
                    color: '#F8FAFC',
                  }}
                />
                <Legend />
                <Bar dataKey="funding" fill="#8B5CF6" name="Funding ($B)" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Pie Chart - Sector Distribution */}
          <div className="p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
            <h3 className="text-xl font-semibold text-white mb-4">Funding by Sector</h3>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={sectorData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                  outerRadius={100}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {sectorData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#1E293B',
                    border: '1px solid #334155',
                    borderRadius: '8px',
                    color: '#F8FAFC',
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>

          {/* AI Analysis Summary */}
          <div className="p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
            <h3 className="text-xl font-semibold text-white mb-4">AI Analysis Summary</h3>
            <div className="prose prose-invert max-w-none">
              <p className="text-slate-300 leading-relaxed mb-4">
                The AI startup ecosystem has experienced remarkable growth from 2020 to 2024, with total funding reaching <strong className="text-blue-400">$127 billion</strong> in 2024, representing a <strong className="text-purple-400">43% year-over-year increase</strong>.
              </p>
              <p className="text-slate-300 leading-relaxed mb-4">
                The United States continues to dominate with $45B in funding, followed by the United Kingdom ($28B) and Germany ($18B). Healthcare AI leads sector investment at 35%, driven by diagnostic tools and personalized medicine applications.
              </p>
              <p className="text-slate-300 leading-relaxed">
                Key trends include increased focus on enterprise AI solutions, growing investment in responsible AI development, and consolidation of smaller players. The market is expected to maintain strong growth through 2025.
              </p>
            </div>

            {/* Sources */}
            <div className="mt-6 pt-6 border-t border-white/10">
              <h4 className="text-sm font-semibold text-slate-400 mb-3">SOURCES</h4>
              <div className="space-y-2">
                {[
                  { title: 'Crunchbase AI Funding Report 2024', url: '#' },
                  { title: 'PitchBook European AI Investment Trends', url: '#' },
                  { title: 'CB Insights State of AI Report', url: '#' },
                  { title: 'TechCrunch AI Funding Analysis', url: '#' },
                ].map((source, index) => (
                  <a
                    key={index}
                    href={source.url}
                    className="block text-sm text-blue-400 hover:text-blue-300 transition-colors"
                  >
                    [{index + 1}] {source.title}
                  </a>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Export Options */}
        <div className="mt-8 p-6 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20 rounded-xl">
          <h3 className="text-xl font-semibold text-white mb-4">Export This Research</h3>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            {['PDF Report', 'PowerPoint', 'PNG Images', 'Markdown', 'JSON Data'].map((format) => (
              <button
                key={format}
                className="px-4 py-3 bg-white/10 hover:bg-white/20 border border-white/20 rounded-lg text-white transition-all text-sm font-medium"
              >
                {format}
              </button>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
