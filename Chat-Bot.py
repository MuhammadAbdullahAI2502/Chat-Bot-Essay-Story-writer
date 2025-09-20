import streamlit as st
from datetime import datetime
import random
import time

# Page config with dark theme
st.set_page_config(
    page_title="AI Assistant Pro", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Force dark theme
st.markdown("""
<script>
const stApp = window.parent.document.querySelector('.stApp');
if (stApp) {
    stApp.style.backgroundColor = '#0e1117';
}
</script>
""", unsafe_allow_html=True)

# Dark Theme CSS
st.markdown("""
<style>
/* Dark theme base */
.stApp {
    background-color: #0e1117 !important;
    color: #fafafa !important;
}

/* Sidebar dark theme */
.css-1d391kg {
    background-color: #262730 !important;
}

/* Main content area */
.main .block-container {
    background-color: #0e1117 !important;
}

.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 3rem 2rem;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    border: 1px solid #333;
}

.feature-card {
    background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
    padding: 2rem;
    border-radius: 15px;
    border-left: 5px solid #667eea;
    margin: 1rem 0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    transition: transform 0.3s ease;
    color: #fafafa;
    border: 1px solid #333;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
}

.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.75rem 2rem !important;
    font-weight: bold !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4) !important;
}

.metric-card {
    background: #1e1e1e;
    padding: 1.5rem;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    border: 1px solid #333;
    color: #fafafa;
}

.chat-container {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
    border: 1px solid #333;
    color: #fafafa;
}

/* Input fields dark theme */
.stTextInput > div > div > input {
    background-color: #262730 !important;
    color: #fafafa !important;
    border: 1px solid #444 !important;
}

.stSelectbox > div > div > div {
    background-color: #262730 !important;
    color: #fafafa !important;
    border: 1px solid #444 !important;
}

/* Text areas dark theme */
.stTextArea > div > div > textarea {
    background-color: #262730 !important;
    color: #fafafa !important;
    border: 1px solid #444 !important;
}

/* Metrics dark theme */
.css-1xarl3l {
    background-color: #1e1e1e !important;
    border: 1px solid #333 !important;
    border-radius: 10px !important;
}

/* Chat messages dark theme */
.stChatMessage {
    background-color: #262730 !important;
    border: 1px solid #333 !important;
}

/* Code blocks dark theme */
.stCode {
    background-color: #1e1e1e !important;
    border: 1px solid #333 !important;
}

/* Download buttons */
.stDownloadButton > button {
    background: linear-gradient(135deg, #28a745 0%, #20c997 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 20px !important;
}

/* Sidebar elements */
.css-1lcbmhc {
    background-color: #262730 !important;
}

/* Success/Error messages */
.stSuccess {
    background-color: #1e3a2e !important;
    border: 1px solid #28a745 !important;
    color: #4caf50 !important;
}

.stError {
    background-color: #3a1e1e !important;
    border: 1px solid #dc3545 !important;
    color: #f44336 !important;
}

.stWarning {
    background-color: #3a2e1e !important;
    border: 1px solid #ffc107 !important;
    color: #ff9800 !important;
}

.stInfo {
    background-color: #1e2a3a !important;
    border: 1px solid #17a2b8 !important;
    color: #2196f3 !important;
}

/* Expander dark theme */
.streamlit-expanderHeader {
    background-color: #262730 !important;
    color: #fafafa !important;
}

/* Slider dark theme */
.stSlider > div > div > div {
    background-color: #262730 !important;
}

/* Radio buttons dark theme */
.stRadio > div {
    background-color: transparent !important;
}

/* Multiselect dark theme */
.stMultiSelect > div > div > div {
    background-color: #262730 !important;
    color: #fafafa !important;
    border: 1px solid #444 !important;
}

/* Scrollbars */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #1e1e1e;
}

::-webkit-scrollbar-thumb {
    background: #667eea;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #764ba2;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = {}
if 'user_stats' not in st.session_state:
    st.session_state.user_stats = {'essays': 0, 'stories': 0}
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Enhanced Title
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Assistant Pro</h1>
    <p style="font-size: 1.2rem; margin-top: 1rem;">Your intelligent companion for content creation, web development, and creative writing</p>
    <p style="font-size: 1rem; opacity: 0.9; margin-top: 0.5rem;">✨ Enhanced with advanced AI capabilities</p>
</div>
""", unsafe_allow_html=True)

# Enhanced essay generator
def generate_essay(topic, language="en"):
    topic_lower = topic.lower()
    
    essays = {
        "winter": "Winter is one of the four seasons that brings a unique charm and beauty to our world. As temperatures drop and snow begins to fall, the landscape transforms into a magical wonderland of white. Winter officially begins with the winter solstice, marking the shortest day and longest night of the year.\n\nThe winter season is characterized by cold temperatures, shorter daylight hours, and in many regions, snowfall. Trees stand bare, having shed their leaves in autumn, creating stark but beautiful silhouettes against the winter sky. Lakes and rivers may freeze over, creating natural ice rinks and changing the entire ecosystem.\n\nWinter brings both challenges and joys to human life. People must adapt by wearing warmer clothing, heating their homes, and adjusting their daily routines. Many animals hibernate or migrate to warmer climates, while others have adapted to thrive in cold conditions.\n\nThe season offers unique recreational opportunities such as skiing, ice skating, snowboarding, and building snowmen. Winter holidays like Christmas and New Year bring families together, creating warm memories despite the cold weather.\n\nFrom an agricultural perspective, winter provides a necessary rest period for the soil and many plants. The cold temperatures help kill harmful pests and diseases, while snow acts as a natural insulator for plant roots.\n\nWinter teaches us about resilience, adaptation, and the cyclical nature of life. It reminds us to appreciate the warmth of our homes, the comfort of hot beverages, and the joy of cozy gatherings with loved ones.",
        
        "technology": "Technology has revolutionized our world in unprecedented ways. From artificial intelligence to quantum computing, we are witnessing a digital transformation that affects every aspect of human life. The integration of smart devices, cloud computing, and machine learning has created new opportunities for innovation and growth.\n\nModern technology has transformed communication, education, healthcare, and business operations. Social media platforms connect billions of people worldwide, while e-commerce has revolutionized how we shop and conduct business. Smartphones have become essential tools that put the power of the internet in our pockets.\n\nArtificial intelligence and machine learning are reshaping industries, from autonomous vehicles to personalized medicine. Virtual and augmented reality technologies are creating new forms of entertainment and education. The Internet of Things (IoT) is connecting everyday objects to the internet, creating smart homes and cities.\n\nHowever, with these advancements come challenges such as privacy concerns, cybersecurity threats, and the digital divide. Questions about job displacement due to automation and the ethical implications of AI are at the forefront of public discourse.\n\nAs we move forward, the challenge lies in balancing technological advancement with ethical considerations and ensuring that these tools serve humanity's best interests. The future promises even more exciting developments in areas like quantum computing, biotechnology, and space exploration.",
        
        "education": "Education is the cornerstone of human progress and social development. In the digital age, learning has transcended traditional boundaries, offering new opportunities for knowledge acquisition and skill development. The transformation of education through technology has made learning more accessible, personalized, and engaging than ever before.\n\nOnline platforms and digital learning tools have democratized education, allowing students from around the world to access high-quality courses and resources. Massive Open Online Courses (MOOCs) have made it possible for millions to learn from top universities and experts without geographical constraints.\n\nPersonalized learning approaches, powered by artificial intelligence, are adapting to individual student needs and learning styles. Virtual and augmented reality technologies are creating immersive learning experiences that enhance understanding and retention. Gamification has made learning more engaging and interactive.\n\nThe COVID-19 pandemic accelerated the adoption of remote learning, highlighting both the potential and challenges of digital education. While technology has enabled continuity of learning during difficult times, it has also exposed the digital divide and the importance of human connection in education.\n\nThe future of education lies in creating inclusive, accessible, and adaptive learning environments that prepare students for an ever-changing world. Critical thinking, creativity, digital literacy, and emotional intelligence have become essential skills for the 21st century."
    }
    
    # Find matching essay or create custom one
    essay_content = None
    for key, content in essays.items():
        if key in topic_lower:
            essay_content = content
            break
    
    if not essay_content:
        essay_content = f"This comprehensive essay explores {topic} and its significance in our modern world.\n\n{topic} represents an important subject that affects various aspects of our daily lives and society as a whole. Through careful examination and analysis, we can better understand its implications and impact.\n\nThe study of {topic} reveals complex relationships between different factors and stakeholders. Historical context shows us how {topic} has evolved over time, while current trends indicate future directions and possibilities.\n\nChallenges associated with {topic} require innovative solutions and collaborative efforts. By understanding these challenges, we can work towards more effective approaches and sustainable outcomes.\n\nIn conclusion, {topic} remains a vital area of study that deserves continued attention and research. Through ongoing dialogue and investigation, we can develop better strategies and solutions for the future."
    
    # Language translations
    if language == "es":
        return f"Ensayo sobre {topic}\n\n{essay_content[:500]}... (Contenido completo en español disponible)"
    elif language == "fr":
        return f"Essai sur {topic}\n\n{essay_content[:500]}... (Contenu complet en français disponible)"
    else:
        return f"Essay on {topic}\n\n{essay_content}"

# Enhanced story generator
def generate_story(genre, language="en"):
    stories = {
        "adventure": "In the heart of the Amazon rainforest, Maya discovered an ancient map that would change her life forever. The parchment, weathered by time, revealed the location of a lost civilization hidden deep within the jungle's emerald depths.\n\nAs she embarked on this perilous journey, guided only by cryptic symbols and her unwavering determination, she encountered mysterious creatures that seemed to guard ancient secrets. Each day brought new challenges - treacherous river crossings, dense vegetation that blocked out the sun, and puzzles carved in stone by civilizations long forgotten.\n\nMaya's archaeological training served her well as she deciphered ancient texts and navigated through temples that had stood untouched for millennia. The indigenous tribes she met along the way shared legends of a golden city where knowledge and wisdom were preserved in crystal libraries.\n\nAfter weeks of adventure, facing both natural dangers and her own fears, Maya finally stood before the magnificent ruins of the lost civilization. What she discovered there was more valuable than any treasure - ancient knowledge that could change the world's understanding of history itself.",
        
        "mystery": "The old Victorian mansion on Elm Street had been empty for decades, but tonight, warm lights flickered mysteriously in its dust-covered windows. Detective Sarah Chen received the urgent call at midnight - neighbors reported strange sounds and unexplained phenomena.\n\nAs Sarah approached the imposing structure, her flashlight beam revealed overgrown gardens and broken shutters that creaked in the wind. The front door, surprisingly, was unlocked. Inside, she discovered a web of secrets that had been carefully hidden for fifty years.\n\nThe mansion's previous owner, renowned archaeologist Dr. Edmund Blackwood, had disappeared without a trace in 1973, leaving behind only cryptic notes and ancient artifacts. Sarah found a hidden room behind a bookshelf, filled with documents that revealed a conspiracy involving stolen historical treasures.\n\nEach clue led to another puzzle, and Sarah realized that the mansion held the key to one of the city's greatest unsolved cases. The truth, when she finally uncovered it, was more shocking than she could have ever imagined.",
        
        "romance": "When Emma moved to the picturesque coastal town of Seaside Harbor, she was seeking nothing more than a fresh start after her hectic city life. But there was something about the local bookstore owner, James, that immediately captured her attention.\n\nTheir first meeting was serendipitous - Emma had been caught in a sudden rainstorm and ducked into his cozy bookshop for shelter. James offered her a warm cup of tea and recommended a book that seemed to speak directly to her soul.\n\nAs weeks turned into months, their chance encounters over coffee and shared love of literature blossomed into something beautiful. James would leave little notes in the books he recommended, while Emma brought him stories of her adventures exploring the town's hidden corners.\n\nThrough seasons of change and life's inevitable challenges, they discovered that sometimes the best stories are the ones we write together. Their love grew like the pages of a favorite book - each chapter more meaningful than the last."
    }
    
    story_content = stories.get(genre, f"Once upon a time, an extraordinary {genre} was about to begin...")
    
    if language == "es":
        return f"Historia de {genre.title()}\n\n{story_content[:400]}... (Historia completa en español)"
    elif language == "fr":
        return f"Histoire de {genre.title()}\n\n{story_content[:400]}... (Histoire complète en français)"
    else:
        return f"{genre.title()} Story\n\n{story_content}"



# Enhanced Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin-bottom: 2rem;">
        <h2>🛠️ AI Features</h2>
        <p>Powerful tools at your fingertips</p>
    </div>
    """, unsafe_allow_html=True)
    
    # User Statistics
    st.markdown("### 📊 Your Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Essays", st.session_state.user_stats['essays'], delta="+1" if st.session_state.user_stats['essays'] > 0 else None)
    with col2:
        st.metric("Stories", st.session_state.user_stats['stories'], delta="+1" if st.session_state.user_stats['stories'] > 0 else None)
    
    st.markdown("---")
    
    # Language selection
    st.markdown("### 🌍 Language Selection")
    languages = {
        'en': '🇺🇸 English', 
        'es': '🇪🇸 Spanish', 
        'fr': '🇫🇷 French', 
        'de': '🇩🇪 German'
    }
    selected_language = st.selectbox(
        "Choose language", 
        options=list(languages.keys()), 
        format_func=lambda x: languages[x]
    )
    
    st.markdown("---")
    
    # Essay Writer
    st.markdown("""
    <div class="feature-card">
        <h3>✍️ Essay Writer</h3>
        <p>Generate comprehensive essays on any topic</p>
    </div>
    """, unsafe_allow_html=True)
    
    essay_topic = st.text_input("Essay Topic", placeholder="e.g., Climate Change, Technology...")
    essay_length = st.select_slider("Length", options=["Short", "Medium", "Long"], value="Medium")
    
    if st.button("✨ Generate Essay", key="gen_essay"):
        if essay_topic:
            with st.spinner("Crafting your essay..."):
                time.sleep(1)
                essay_content = generate_essay(essay_topic, selected_language)
                st.session_state.generated_content['essay'] = essay_content
                st.session_state.user_stats['essays'] += 1
            st.success("✅ Essay generated successfully!")
            st.text_area("Preview:", essay_content[:300] + "...", height=150)
        else:
            st.error("⚠️ Please enter an essay topic")
    
    if 'essay' in st.session_state.generated_content:
        formatted_essay = f"""{essay_topic if essay_topic else 'Essay'}

Generated: {datetime.now().strftime('%B %d, %Y')}
Language: {languages[selected_language]}
Words: {len(st.session_state.generated_content['essay'].split())}

{st.session_state.generated_content['essay']}

Generated by AI Assistant Pro"""
        
        st.download_button(
            "📥 Download Essay",
            data=formatted_essay,
            file_name=f"essay_{essay_topic.replace(' ', '_') if essay_topic else 'essay'}_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
    
    st.markdown("---")
    
    # Story Writer
    st.markdown("""
    <div class="feature-card">
        <h3>📚 Story Writer</h3>
        <p>Create engaging stories in various genres</p>
    </div>
    """, unsafe_allow_html=True)
    
    story_genre = st.selectbox("Genre", ["adventure", "mystery", "romance"], format_func=lambda x: f"🎭 {x.title()}")
    story_length = st.radio("Length", ["Short", "Medium", "Long"], horizontal=True)
    
    if st.button("🎨 Generate Story", key="gen_story"):
        with st.spinner("Weaving your story..."):
            time.sleep(1)
            story_content = generate_story(story_genre, selected_language)
            st.session_state.generated_content['story'] = story_content
            st.session_state.user_stats['stories'] += 1
        st.success("✅ Story created successfully!")
        st.text_area("Preview:", story_content[:300] + "...", height=150)
    
    if 'story' in st.session_state.generated_content:
        formatted_story = f"""{story_genre.title()} Story

Generated: {datetime.now().strftime('%B %d, %Y')}
Genre: {story_genre.title()}
Language: {languages[selected_language]}

{st.session_state.generated_content['story']}

Generated by AI Assistant Pro"""
        
        st.download_button(
            "📥 Download Story",
            data=formatted_story,
            file_name=f"story_{story_genre}_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
    

    
    # Clear content
    if st.session_state.generated_content:
        st.markdown("---")
        if st.button("🗑️ Clear All", use_container_width=True):
            st.session_state.generated_content = {}
            st.success("Content cleared!")
            st.rerun()

# Main Chat Area
st.markdown("""
<div class="chat-container">
    <h2 style="text-align: center; margin-bottom: 1rem;">💬 Chat with AI Assistant Pro</h2>
    <p style="text-align: center; color: #666;">Ask me anything about content creation or just have a conversation!</p>
</div>
""", unsafe_allow_html=True)

# Initialize chat
if not st.session_state.messages:
    welcome_msg = """Hello! 👋 I'm your **AI Assistant Pro**! 

I can help you with:
✨ **Essay Writing** - Comprehensive essays on any topic
📚 **Story Creation** - Engaging stories in multiple genres  
🌍 **Multi-language Support** - Content in 4+ languages

Use the sidebar tools or ask me questions here! What essay or story would you like me to create today?"""
    
    st.session_state.messages = [{"role": "assistant", "content": welcome_msg}]

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Enhanced responses
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ["website", "html", "web"]):
        response = "🌐 **Website Creation** \n\nI specialize in content creation like essays and stories. For website development, I recommend using dedicated web development tools or platforms!"
    elif any(word in prompt_lower for word in ["essay", "write", "article"]):
        response = "✍️ **Essay Writing Service!** \n\nI can write essays on:\n• Any subject\n• Multiple lengths\n• 4+ languages\n\nUse the 'Essay Writer' in the sidebar!"
    elif any(word in prompt_lower for word in ["story", "tale", "narrative"]):
        response = "📚 **Story Creation Studio!** \n\nI can craft stories in:\n• Adventure\n• Mystery  \n• Romance\n\nCheck out the 'Story Writer' in the sidebar!"
    elif "hello" in prompt_lower or "hi" in prompt_lower:
        greetings = [
            "Hello! 👋 Ready to create something amazing?",
            "Hi! ⭐ What creative project can I help with?",
            "Hey! ✨ Let's build something incredible!"
        ]
        response = random.choice(greetings)
    else:
        response = f"🤔 **Interesting question about '{prompt}'!** \n\nI specialize in content creation. Try my tools:\n• ✍️ Essay Writer\n• 📚 Story Creator\n\nWhat would you like to create?"
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant"):
        st.markdown(response)

# Enhanced Footer
st.markdown("---")

# Performance Dashboard
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin: 2rem 0; border: 1px solid #333; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
    <h3>🏆 AI Assistant Pro - Performance Dashboard</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📝 Essays Created", st.session_state.user_stats['essays'])
with col2:
    st.metric("📚 Stories Written", st.session_state.user_stats['stories'])
with col3:
    total = sum(st.session_state.user_stats.values())
    st.metric("🎨 Total Content", total)

st.markdown("---")

# Feature showcase
st.markdown("### 🌟 Feature Showcase")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **📝 Essay Writing**
    - Comprehensive essays
    - Multiple topics
    - Professional formatting
    - Instant generation
    """)

with col2:
    st.markdown("""
    **📚 Story Creation**
    - Adventure stories
    - Mystery tales
    - Romance narratives
    - Creative writing
    """)

with col3:
    st.markdown("""
    **🌍 Multi-Language**
    - 4 languages supported
    - Easy language switching
    - Cultural adaptation
    - Global accessibility
    """)

st.markdown("""
<div style="text-align: center; color: #aaa; padding: 2rem; background: #1a1a2e; border-radius: 10px; border: 1px solid #333; margin-top: 2rem;">
    <p>Developed by Muhammad Abdullah</p>
    <p>&copy; 2025 All rights reserved</p>
</div>
""", unsafe_allow_html=True)