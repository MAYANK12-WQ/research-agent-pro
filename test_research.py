"""
Simple test script to verify research agent is working
"""
import requests
import json

# Test the research endpoint
def test_research(query):
    print(f"\n{'='*60}")
    print(f"Testing Research Agent")
    print(f"{'='*60}")
    print(f"\nQuery: {query}")
    print(f"\nSending request to http://localhost:8000/api/v1/research/...")

    try:
        response = requests.post(
            "http://localhost:8000/api/v1/research/",
            json={"query": query},
            timeout=60
        )

        if response.status_code == 200:
            data = response.json()

            print(f"\n✅ SUCCESS!")
            print(f"\nStatus: {data.get('status')}")
            print(f"Query: {data.get('query')}")
            print(f"\n📊 Charts Generated: {len(data.get('charts', []))}")

            for i, chart in enumerate(data.get('charts', []), 1):
                print(f"  {i}. {chart.get('type').upper()} - {chart.get('title')}")

            print(f"\n🎨 Infographics Generated: {len(data.get('infographics', []))}")

            for i, infographic in enumerate(data.get('infographics', []), 1):
                print(f"  {i}. {infographic.get('type').upper()} - {infographic.get('title')}")

            print(f"\n📚 Sources Found: {len(data.get('sources', []))}")

            for i, source in enumerate(data.get('sources', [])[:5], 1):
                print(f"  {i}. {source.get('title', 'No title')}")

            print(f"\n💡 AI Insights:")
            insights = data.get('insights', {})
            summary = insights.get('summary', 'No summary available')
            print(f"  {summary[:200]}...")

            print(f"\n✨ Key Insights:")
            for i, insight in enumerate(insights.get('key_insights', []), 1):
                print(f"  {i}. {insight}")

            print(f"\n{'='*60}")
            print(f"✅ RESEARCH AGENT IS WORKING PERFECTLY!")
            print(f"{'='*60}\n")

            # Save full response
            with open('research_result.json', 'w') as f:
                json.dump(data, f, indent=2)
            print(f"💾 Full response saved to: research_result.json")

        else:
            print(f"\n❌ ERROR: HTTP {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.ConnectionError:
        print(f"\n❌ ERROR: Cannot connect to backend")
        print(f"Make sure the backend is running on http://localhost:8000")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")


if __name__ == "__main__":
    # Test query
    query = "AI startup funding trends in Europe 2024"
    test_research(query)
